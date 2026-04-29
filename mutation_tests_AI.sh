#!/bin/bash

cosmic-ray init ray-config_AI.toml mutants_AI.sqlite --force
cosmic-ray --verbosity=INFO baseline ray-config_AI.toml
cosmic-ray exec ray-config_AI.toml mutants_AI.sqlite
cr-html mutants_AI.sqlite > report_AI.html