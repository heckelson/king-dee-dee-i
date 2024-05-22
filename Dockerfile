# syntax=docker/dockerfile:1.4

## Build

FROM node:18-alpine AS builder
RUN echo "test1"
RUN file="$(ls -1 /tmp/dir)" && echo $file
WORKDIR /data/frontend
RUN echo "test2"
RUN file="$(ls -1 /tmp/dir)" && echo $file

COPY package.json .
RUN corepack enable && corepack prepare

COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build