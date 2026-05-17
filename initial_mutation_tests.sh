#!/bin/bash

cosmic-ray init ray-config.toml initial_mutants.sqlite --force
cosmic-ray --verbosity=INFO baseline ray-config.toml
cosmic-ray exec ray-config.toml initial_mutants.sqlite
cr-html initial_mutants.sqlite > initial_report.html