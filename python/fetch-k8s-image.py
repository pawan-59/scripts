import subprocess as sp
import requests
import sys
DASHBOARD=sp.getoutput("kubectl get po -ndevtroncd  -l component=dashboard  -o jsonpath='{.items[0].spec.containers[*].image}'")
ORCHESTRATOR=sp.getoutput("kubectl get po -ndevtroncd -l component=devtron -o jsonpath='{.items[0].spec.containers[*].image}'")
#MIGRATOR=sp.getoutput("kubectl get po -ndevtroncd -l component=postgresql-migrate-devtron -o jsonpath='{.items[0].spec.containers[*].image}'")
IMAGE_SCANNER=sp.getoutput("kubectl get po -ndevtroncd -l component=image-scanner -o jsonpath='{.items[0].spec.containers[*].image}'")
NOTIFIER=sp.getoutput("kubectl get pod -l component=notifier -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
KUBEWATCH=sp.getoutput("kubectl get pod -l app=kubewatch -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
GIT_SENSOR=sp.getoutput("kubectl get po -l app=git-sensor  -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
LENS=sp.getoutput("kubectl get pod -l component=lens -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
CLAIR=sp.getoutput("kubectl get po -l component=clair -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
ROLLOUT=sp.getoutput("kubectl get po -l app.kubernetes.io/name=argo-rollouts -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
NATS_SERVER=sp.getoutput("kubectl get po devtron-nats-1    -ndevtroncd -o jsonpath='{.spec.containers[*].image}'")
NATS_POD=sp.getoutput("kubectl get po -ndevtroncd -l app=nats-streaming -o name |awk 'FNR == 2' |awk -F \"/\" '{print $2}'")
NATS_STREAM=sp.getoutput("kubectl get po %s   -ndevtroncd -o jsonpath='{.spec.containers[*].image}'"%NATS_POD)

CLUSTER=sys.argv[1]
buffer=('CLUSTER: %s\n'%CLUSTER)
buffer+=("MicroServices   Imaage\n")
buffer+=("-------------   -------\n")
buffer+=("DashBoard:      %s\n"%DASHBOARD)
buffer+=("Orchestrator:   %s\n"%ORCHESTRATOR)
#buffer+=("Migrator:       %s\n"%MIGRATOR)
buffer+=("Image-Scanner:  %s\n"%IMAGE_SCANNER)
buffer+=("Notifier:       %s\n"%NOTIFIER)
buffer+=("Kubewatch:      %s\n"%KUBEWATCH)
buffer+=("Git-Snesor:     %s\n"%GIT_SENSOR)
buffer+=("Lens:           %s\n"%LENS)
buffer+=("Clair:          %s\n"%CLAIR)
buffer+=("Rollout:        %s\n"%ROLLOUT)
buffer+=("Nats-server:    %s\n"%NATS_SERVER)
buffer+=("Nats-stream:    %s\n"%NATS_STREAM)

print(buffer)

APP_SLACK_WEBHOOK="webhook link"
resp = requests.post(
            APP_SLACK_WEBHOOK,
            data={
                'content':"\n\n```\n" + buffer + "\n```",
            },
        )
