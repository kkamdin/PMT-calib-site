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
	firefox "http://127.0.0.1:8000"

stop:
	# This stops the test server. So nasty.
	ps axuww | grep SimpleHTTPServer | grep -v grep | head -1 | awk '{ print $$2 }' | xargs kill

clean:
	@echo "==> Cleaning"
	rm -f lib/*.pyc libexec/*.pyc data/run*/*_cache.py*
	rm -rf data/run*/channel_data

jsdeps: lib/eca_constants.json data/index.json

lib/eca_constants.json: lib/eca_constants.py
	@echo "==> Generating eca_constants.json"
	libexec/generate_constants_json.py > lib/eca_constants.json

data/index.json: data/run*
	@echo "==> Generating index.json"
	libexec/generate_index_json.py data/run* >data/index.json

parse:
	@for RUN in data/run*; do \
		echo "==> Parsing .ratdb files in $${RUN}"; \
		OUTPUT_DIR="$${RUN}/channel_data"; \
		mkdir "$${OUTPUT_DIR}"; \
		echo "====> currently PDST only "; \
		if [ -e $${RUN}/PDST_*.ratdb ]; then \
			/usr/bin/time $(PYPY) libexec/parse_ratdb.py \
				--pythonsrc "$${RUN}/pdst_cache.py" \
				$${RUN}/PDST_*.ratdb; \
		fi; \
	done

rootToPNG:
	@for RUN in data/run*; do \
		echo "==> Formatting ECA histograms $${RUN}"; \
		OUTPUT_DIR="$${RUN}/formattedPDSThistograms"; \
		mkdir "$${OUTPUT_DIR}"; \
		echo "====> retrieving PDST histograms "; \
		if [ -e $${RUN}/PDSThists_*.ratdb ]; then \
			/usr/bin/time $(PYPY) libexec/generate_formatted_histos.py \
				$${RUN}/PDSThists_*.ratdb; \
		fi; \
	done
index:
	@for RUN in data/run*; do \
		echo "==> Generating .json files in $${RUN}"; \
		OUTPUT_DIR="$${RUN}/channel_data"; \
		echo "====> PDST"; \
		if [ -e $${RUN}/pdst_cache.py ]; then \
		/usr/bin/time libexec/generate_flag_index_json.py \
			--pdst "$${RUN}/pdst_cache.py" \
			>$${OUTPUT_DIR}/pdst_flag_index.json; \
		fi; \
		echo "====> TSLP"; \
		if [ -e $${RUN}/tslp_cache.py ]; then \
		/usr/bin/time libexec/generate_flag_index_json.py \
			--tslp "$${RUN}/tslp_cache.py" \
			>$${OUTPUT_DIR}/tslp_flag_index.json; \
		fi; \
	done


# use set -x to debug
generate:
	@for RUN in data/run*; do \
		echo "==> Generating channel flag status images for $${RUN}"; \
		OUTPUT_DIR="$${RUN}/channel_data"; \
		echo "====> PDST "; \
		if [ -e $${RUN}/pdst_cache.py ]; then \
			/usr/bin/time libexec/generate_images.py \
				--pdst "$${RUN}/pdst_cache.py" \
				--directory "$${OUTPUT_DIR}" \
				--scale=2; \
		fi; \
		echo "====> TSLP "; \
		if [ -e $${RUN}/tslp_cache.py ]; then \
			/usr/bin/time libexec/generate_images.py \
				--tslp "$${RUN}/tslp_cache.py" \
				--directory "$${OUTPUT_DIR}" \
				--scale=2; \
		fi; \
	done
