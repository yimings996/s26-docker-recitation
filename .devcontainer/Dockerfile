FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# Remove broken Yarn GPG key / repo so apt-get update succeeds
RUN rm -f /etc/apt/sources.list.d/yarn.list /usr/share/keyrings/yarnkey.gpg