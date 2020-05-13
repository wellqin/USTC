### 基础知识补充

dangling是一种特殊的,不会再被使用到的镜像,docker有专门清理dangling镜像的命令
1. dangling镜像通过命令 docker image prune -f 清理。
2. 通过命令 docker images | awk 'NR!=1{print $1":"$2}' | xargs docker rmi 可以批量清除无用的镜像，
且不会影响使用中的镜像和基础镜像。
