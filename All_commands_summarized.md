# Docker Mastery: Essential Commands Summary

## 🐳 Containers
### Lifecycle Management
* `docker run <image>`: Create and start a new container from an image.
    * `-it`: Run **interactively** (connects your terminal to the container).
    * `-d`: Run in **detached** mode (runs in the background).
    * `-p 8000:8000`: Publish **ports**. `Host(left) : Container(right)`.
    * `--name <name>`: Assign a specific name to the container for easier management.
    * `--rm`: Automatically **remove** the container filesystem when it stops.
* `docker stop <name|ID>`: Gracefully stop a running container.
* `docker start <name|ID>`: Start a previously created/stopped container.
    * `-i`: Attach interactive standard input.
* `docker rm <ID>`: Remove a stopped container.
    * `-f`: **Force** remove a container (even if it is currently running).

### Inspection & Debugging
* `docker ps`: List only **running** containers.
* `docker ps -a`: List **all** containers (including exited/stopped ones).
* `docker logs <ID>`: Fetch the logs of a container.
    * `-f`: **Follow** log output (real-time streaming).
* `docker inspect <ID>`: Return low-level information on Docker objects in JSON format.
* `docker stats`: Display a live stream of container(s) **resource usage** statistics.
* `docker top <ID>`: Display the running processes of a container.
* `docker cp <ID>:<path> <local_path>`: **Copy** files/folders between a container and the local filesystem.

---

## 🖼️ Images
### Dockerfile Instructions
* `FROM`: Defines the **Base Image** to start the build process.
* `WORKDIR`: Sets the **working directory** for any subsequent instructions (RUN, CMD, etc.).
* `COPY <src> <dest>`: Copies files or directories from the host into the image.
* `EXPOSE`: Documentation flag indicating which **ports** the application listens on.
* `CMD`: Specifies the default command to execute when the container starts.

### Image Management
* `docker build -t <name> <path>`: Build an image from a Dockerfile. Use `.` for the current directory.
* `docker images`: List all locally available images.
* `docker rmi <image>`: **Remove** one or more images.
* `docker tag <source_image> <target_image:tag>`: Create a **tag** (alias) that refers to a source image.
* `docker system prune`: **Clean up** unused data (stopped containers, unused networks, dangling images).

---

## ☁️ Docker Hub (Registry)
* `docker login`: Log in to a Docker registry (default is Docker Hub).
* `docker logout`: Log out from a Docker registry.
* `docker pull <image>`: **Download** an image from the registry to your local machine.
* `docker push <username/image:tag>`: **Upload** a local image to the registry.
    * *Note: The image must be tagged with your Docker Hub username to push successfully.*

---

## 💾 Volumes & Bind Mounts
* **Bind Mount**: Maps a specific host path to a container path.
    * `docker run -v C:/local/path:/container/path <image>`
    * **Simple Bind Mount**: Used for data persistence of specific path (ex.: databases).
    * **Project Update**: Mounts the root project to the `WORKDIR` for real-time code updates.
* **Named Volume**: Managed by Docker, best for database persistence.
    * `docker run -v my_data:/var/lib/mysql <image>`
* **Create volumes manually**
    * `docker volume create <name>`
* **List Volumes**
    * `docker volume ls`
* **Remove Volumes**
    * `docker rm <nome>`
* **Clean up unused volumes**
    * `docker volume prune`
* **Read only volumes**
    * `docker run -v volume:/data:ro`