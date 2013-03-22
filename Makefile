.PHONY: rebuild clean jsdeps parse index generate
PYPY = `which pypy`
# This Makefile will use the pypy version of python for ratdb parsing if it can.
# If so, your copy of pypy will need access to the pyyaml module.
# As of this writing, I'm still using the regular version of python for image
# generation because it appears to be MUCH faster for that task.
# If you don't have pypy or something is going astray, just define PYPY
# as an empty string above.
#
# OS X user hint:
# brew install pypy
# you *might* need to /usr/local/share/pypy/easy_install pip
# /usr/local/share/pypy/pip install pyyaml

rebuild: clean parse generate index jsdeps

test:
	@echo "==> Starting test server"
	(cd www && python -m "SimpleHTTPServer" &)
	open "http://127.0.0.1:8000"

stop:
	# This stops the test server. So nasty.
	ps axuww | grep SimpleHTTPServer | grep -v grep | head -1 | awk '{ print $$2 }' | xargs kill

clean:
	@echo "==> Cleaning"
	rm -f lib/*.pyc libexec/*.pyc data/run*/*_cache.py*
	rm -rf data/run*/channel_data

jsdeps: lib/pca_constants.json data/index.json

lib/pca_constants.json: lib/pca_constants.py
	@echo "==> Generating pca_constants.json"
	libexec/generate_constants_json.py > lib/pca_constants.json

data/index.json: data/run*
	@echo "==> Generating index.json"
	libexec/generate_index_json.py data/run* >data/index.json

parse:
	@for RUN in data/run*; do \
		echo "==> Parsing .ratdb files in $${RUN}"; \
		OUTPUT_DIR="$${RUN}/channel_data"; \
		mkdir "$${OUTPUT_DIR}"; \
		echo "====> General "; \
		if [ -e $${RUN}/PCA_log_*.ratdb ]; then \
			/usr/bin/time $(PYPY) libexec/parse_ratdb.py \
				--pythonsrc "$${RUN}/general_cache.py" \
				--generalpath "$${OUTPUT_DIR}/general_summary.txt" \
				$${RUN}/PCA_log_*.ratdb; \
		fi; \
		echo "====> Gain Fit"; \
		if [ -e $${RUN}/PCAGF_*.ratdb ]; then \
		/usr/bin/time $(PYPY) libexec/parse_ratdb.py \
			--pythonsrc "$${RUN}/gainfit_cache.py" \
			--gainfitpath "$${OUTPUT_DIR}/gainfit_summary.txt" \
			$${RUN}/PCAGF_*.ratdb; \
		fi; \
		echo "====> Time Walk"; \
		if [ -e $${RUN}/PCATW_*.ratdb ]; then \
		/usr/bin/time $(PYPY) libexec/parse_ratdb.py \
			--pythonsrc "$${RUN}/timewalk_cache.py" \
			--timewalkpath "$${OUTPUT_DIR}/timewalk_summary.txt" \
			$${RUN}/PCATW_*.ratdb; \
		fi; \
	done

index:
	@for RUN in data/run*; do \
		echo "==> Generating .json files in $${RUN}"; \
		OUTPUT_DIR="$${RUN}/channel_data"; \
		echo "====> Gain Fit"; \
		if [ -e $${RUN}/gainfit_cache.py ]; then \
		/usr/bin/time libexec/generate_flag_index_json.py \
			--gainfit "$${RUN}/gainfit_cache.py" \
			>$${OUTPUT_DIR}/gf_flag_index.json; \
		fi; \
		echo "====> Time Walk"; \
		if [ -e $${RUN}/timewalk_cache.py ]; then \
		/usr/bin/time libexec/generate_flag_index_json.py \
			--timewalk "$${RUN}/timewalk_cache.py" \
			>$${OUTPUT_DIR}/tw_flag_index.json; \
		fi; \
	done


# use set -x to debug
generate:
	@for RUN in data/run*; do \
		echo "==> Generating channel flag status images for $${RUN}"; \
		OUTPUT_DIR="$${RUN}/channel_data"; \
		echo "====> Gain Fit "; \
		if [ -e $${RUN}/gainfit_cache.py ]; then \
			/usr/bin/time libexec/generate_images.py \
				--gainfit "$${RUN}/gainfit_cache.py" \
				--directory "$${OUTPUT_DIR}" \
				--scale=2; \
		fi; \
		echo "====> Time Walk "; \
		if [ -e $${RUN}/timewalk_cache.py ]; then \
			/usr/bin/time libexec/generate_images.py \
				--timewalk "$${RUN}/timewalk_cache.py" \
				--directory "$${OUTPUT_DIR}" \
				--scale=2; \
		fi; \
	done
