# streaming-poc
A quick PoC to play around with streaming

Using Skaffold with Helm
https://skaffold.dev/docs/pipeline-stages/deployers/helm/

Some timing issues, when starting everything with `skaffold dev`, things don't work from the start; you have to install cert manager first, then redpanda operator, then the red panda cluster.