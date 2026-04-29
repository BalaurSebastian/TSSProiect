#!/bin/bash

cosmic-ray init ray-config_AI.toml initial_mutants_AI.sqlite --force
cosmic-ray --verbosity=INFO baseline ray-config_AI.toml
cosmic-ray exec ray-config_AI.toml initial_mutants_AI.sqlite
cr-html initial_mutants_AI.sqlite > initial_report_AI.html