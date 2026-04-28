#!/bin/bash

cosmic-ray init ray-config.toml mutants.sqlite --force
cosmic-ray --verbosity=INFO baseline ray-config.toml
cosmic-ray exec ray-config.toml mutants.sqlite
cr-html mutants.sqlite > report.html