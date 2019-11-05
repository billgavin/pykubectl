import fire
from kubernetes import client, config

def create_container_object(container_name, image, *container_ports):
	container = client.V1Container(
		name = container_name,
		image = images,
		ports = [client.V1ContainerPort(container_port=i) for i in list(container_ports)]
	)
	return container

def create_deployment_object(deployment_name, app_label, replicas, *containers):
	template = client.V1PodTemplateSpec(
		metadata = client.V1ObjectMeta(labels={'app': app_label}),
		spec = client.V1PodSpec(containers=list(containers))
	)
	spec = client.V1DeploymentSpec(
		replicas = replicas,
		template = template,
		selector = {'matchLabels': {'app': app_label}}
	)
	deployment = client.V1Deployment(
		api_version = "apps/v1",
		kind = "Deployment",
		metadata = client.V1ObjectMeta(name=deployment_name),
		spec = spec
	)
	return deployment

def create_deployment(api_instance, deployment, namespace='default'):
	api_resp = api_instance.create_namespaced_deployment(
		body = deployment,
		namespace = namespace
	)
	print("Deployment created. status='%s'" % str(api_resp.status))
