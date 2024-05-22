# syntax=docker/dockerfile:1.4

## Build

FROM node:18-alpine AS builder
WORKDIR /data/frontend

COPY package.json .
RUN corepack enable && corepack prepare

COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build