from kubernetes import client, config, utils
import yaml
import logging
import os

def run(body):
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    logging.basicConfig(format="%(module)s [%(levelname)s] %(message)s", level=getattr(logging, LOG_LEVEL))
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, LOG_LEVEL))
    try:
        config.load_kube_config()
        v1 = client.CustomObjectsApi()
        v1.create_namespaced_custom_object(
            group="monitoring.spotahome.com",
            version="v1alpha1",
            namespace="monitoring",
            plural="servicelevels",
            body=yaml.load(body, Loader=yaml.FullLoader)
        )
    except:
        logger.info("Failed to apply slo component, crd object not present")

