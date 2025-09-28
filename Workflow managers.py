from prefect import flow, task
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime


# ---- Task 1: Ejecutar Nmap ----
@task
def run_nmap_scan(target="scanme.nmap.org", ports="80,443"):
    """
    Ejecuta un escaneo nmap y guarda el resultado en XML.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"nmap_results_{timestamp}.xml"
    command = ["nmap", "-p", ports, "-oX", output_file, target]
    subprocess.run(command, check=True)
    return output_file


# ---- Task 2: Procesar Resultados ----
@task
def parse_nmap_results(xml_file):
    """
    Parsea el archivo XML de Nmap y extrae host, puerto y estado.
    """
    results = []
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for host in root.findall('host'):
        address = host.find('address').get('addr')
        for port in host.findall(".//port"):
            port_id = port.get('portid')
            state = port.find('state').get('state')
            service_el = port.find('service')
            service = service_el.get('name') if service_el is not None else "desconocido"
            results.append({
                "host": address,
                "port": port_id,
                "state": state,
                "service": service
            })
    return results


# ---- Task 3: Generar Reporte ----
@task
def generate_report(scan_results):
    """
    Genera un reporte simple en texto con los resultados.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"scan_report_{timestamp}.txt"
    with open(report_file, "w") as f:
        f.write("Reporte de Escaneo Nmap\n")
        f.write("=========================\n\n")
        for r in scan_results:
            f.write(f"Host: {r['host']} | Puerto: {r['port']} | Estado: {r['state']} | Servicio: {r['service']}\n")
    return report_file


# ---- Flow Principal ----
@flow
def nmap_scan_flow(target="scanme.nmap.org", ports="80,443"):
    xml_file = run_nmap_scan(target, ports)
    scan_results = parse_nmap_results(xml_file)
    report = generate_report(scan_results)
    print(f"Reporte generado: {report}")


if __name__ == "__main__":
    # Ejecutar el flujo manualmente:
    nmap_scan_flow(target="scanme.nmap.org", ports="80,443")
