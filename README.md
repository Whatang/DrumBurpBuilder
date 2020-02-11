# DrumBurp Builder

DrumBurp is an open source drum notation editor, available from www.whatang.org. This repository contains the files needed to set up a docker image for building DrumBurp.

## Repo contents

This directory contains the definition of the docker image. `.github\workflows` defines how GitHub Actions builds and pushes these images to DockerHub.

### environment

The environment directory contains the information needed to set up an environemt for developing DrumBurp.

### install

The install directory contains scripts used by the Dockerfile to install necessary software for DrumBurp to be built.

## Building the Docker image

The image can be built automatically by GitHub Actions on a push to GitHub, or it can be built by hand with

    docker build -f Dockerfile.windows -t whatang/db-builder-windows:<version number> -t whatang/db-builder-windows:latest .

## Building DrumBurp using the Docker image

The image is set up to assume that the DrumBurp source repo is mounted in a container at `C:\build\DrumBurp`. Running a container with the source mounted in this way will run the `build\build_windows.ps1` PowerShell script in the repo.
