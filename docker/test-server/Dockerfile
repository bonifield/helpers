# much more complex example of using uv in Docker, along with multi-stage builds
# speeds up the build process and produces smaller final containers

# derived from:
#   https://depot.dev/docs/container-builds/how-to-guides/optimal-dockerfiles/python-uv-dockerfile
#   https://docs.astral.sh/uv/guides/integration/docker/

#####################
# BUILDER
# this stage "walks" so the runtime stage can "run" (faster)
#####################

# create builder stage
FROM python:3.13-slim AS build

# download uv files
COPY --from=ghcr.io/astral-sh/uv:0.9.8 /uv /uvx /bin/

# change to /app
WORKDIR /app

# tell uv to compile bytecode and copy files, not symlinks
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# add the uv lock and toml files
COPY uv.lock pyproject.toml ./

# use a Docker build cache for the uv cache directory that persists across builds
# target is mount point for uv cache
# install dependencies only, not the application itself
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-dev

# copy the application on its own layer
COPY app.py .

# install app without updating lock file
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

#####################
# RUNTIME
#####################

FROM python:3.13-slim AS runtime

# add virtual environment to path
ENV PATH="/app/.venv/bin:$PATH"
# BE SURE TO SET FLASK_APP AND FLASK_RUN_HOST IN docker-compose.yml
# OTHERWISE FLASK LISTENS ON LOCALHOST

# create user and group for the application
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -m -d /app -s /bin/false appuser

# change working directories
WORKDIR /app

# copy application state from build into runtime, change ownership
COPY --from=build --chown=appuser:appgroup /app .

# open this port
EXPOSE 5000

# switch to the unprivileged user
USER appuser

# uses virtual environment python
# use this is not specifying FLASK_APP environment variable
#ENTRYPOINT ["python", "-m", "flask", "--app", "app.py", "run"]
ENTRYPOINT ["python", "-m", "flask", "run"]
