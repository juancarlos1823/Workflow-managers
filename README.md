# Nmap Scanner con Prefect

Un sistema automatizado de escaneo de red usando Nmap y Prefect para la orquestación de flujos de trabajo.

## 📋 Descripción

Este proyecto automatiza el proceso de escaneo de red utilizando Nmap, procesando los resultados y generando reportes legibles. Utiliza Prefect para la orquestación de tareas, proporcionando un flujo de trabajo robusto y escalable.

### Características principales:
- ✅ Escaneo automatizado de puertos con Nmap
- ✅ Procesamiento de resultados XML
- ✅ Generación de reportes en formato texto
- ✅ Orquestación con Prefect
- ✅ Timestamps automáticos para archivos
- ✅ Manejo de errores integrado

## 🛠️ Requisitos

### Software necesario:
- Python 3.7+
- Nmap instalado en el sistema
- Prefect 2.x

### Dependencias Python:
\`\`\`bash
prefect>=2.0.0
\`\`\`

## 📦 Instalación

1. **Clonar o descargar el proyecto**
\`\`\`bash
git clone <tu-repositorio>
cd nmap-scanner
\`\`\`

2. **Instalar dependencias**
\`\`\`bash
pip install prefect
\`\`\`

3. **Verificar instalación de Nmap**
\`\`\`bash
nmap --version
\`\`\`

## 🚀 Uso

### Ejecución básica
\`\`\`bash
python run-nmap-scan.py
\`\`\`

### Personalizar objetivo y puertos
Modifica las variables en el archivo o ejecuta directamente:
\`\`\`python
from run_nmap_scan import nmap_scan_flow

# Escanear un objetivo específico
nmap_scan_flow(target="192.168.1.1", ports="22,80,443,8080")

# Escanear rango de puertos
nmap_scan_flow(target="example.com", ports="1-1000")
\`\`\`

### Con Prefect UI
\`\`\`bash
# Iniciar servidor Prefect (opcional)
prefect server start

# Ejecutar el flujo
python run-nmap-scan.py
\`\`\`

## 📁 Estructura del Proyecto

\`\`\`
nmap-scanner/
├── run-nmap-scan.py          # Script principal
├── README.md                 # Este archivo
├── nmap_results_*.xml        # Resultados XML (generados)
└── scan_report_*.txt         # Reportes finales (generados)
\`\`\`

## 🔧 Componentes del Código

### Tasks (Tareas)

1. **`run_nmap_scan(target, ports)`**
   - Ejecuta el comando Nmap
   - Guarda resultados en XML con timestamp
   - Parámetros configurables

2. **`parse_nmap_results(xml_file)`**
   - Parsea el archivo XML de Nmap
   - Extrae información de hosts, puertos y servicios
   - Retorna lista estructurada de resultados

3. **`generate_report(scan_results)`**
   - Genera reporte legible en texto plano
   - Incluye timestamp y formato organizado
   - Guarda archivo con nombre único

### Flow (Flujo)

**`nmap_scan_flow(target, ports)`**
- Orquesta las tres tareas en secuencia
- Maneja el flujo de datos entre tareas
- Proporciona logging automático

## 📊 Ejemplo de Salida
<img width="1500" height="490" alt="image" src="https://github.com/user-attachments/assets/08cf166d-be99-43e4-bf6b-d0dd90a0587f" />

### Archivo de reporte generado:

<img width="1735" height="638" alt="image" src="https://github.com/user-attachments/assets/67887e3c-535c-470c-9c52-a569b348d835" />

### Para programar una rutina lo puedes hacer con el siguiente codigo
1️⃣ Abrir la terminal

Puedes usar PowerShell, CMD o la terminal de PyCharm (el panel inferior donde puedes escribir comandos).

2️⃣ Ir a la carpeta donde está tu script Python
Por ejemplo:

cd "C:\Users\USER\PycharmProjects\Tolerante a fallas\Workflow managers"


3️⃣ Construir el deployment
Ejecuta:

prefect deployment build "Workflow managers.py":nmap_scan_flow -n "Escaneo Nocturno"


Esto:

Busca en Workflow managers.py la función nmap_scan_flow.

Crea un archivo YAML (por defecto nmap_scan_flow-deployment.yaml).

4️⃣ Aplicar el deployment

prefect deployment apply nmap_scan_flow-deployment.yaml


Esto registra el deployment en tu servidor Prefect local.

5️⃣ Arrancar un agente Prefect

prefect agent start


Esto lanza un agente que escucha jobs pendientes y ejecuta el flujo según la programación que configures.

Reporte de Escaneo Nmap
=========================

Host: 45.33.32.156 | Puerto: 80 | Estado: open | Servicio: http
Host: 45.33.32.156 | Puerto: 443 | Estado: open | Servicio: https
\`\`\`

## ⚙️ Configuración Avanzada

### Modificar parámetros de Nmap
\`\`\`python
# En la función run_nmap_scan, puedes agregar más opciones:
command = ["nmap", "-p", ports, "-sV", "-O", "-oX", output_file, target]
\`\`\`

### Personalizar formato de reporte
Modifica la función `generate_report()` para cambiar el formato de salida.

## 🔒 Consideraciones de Seguridad

⚠️ **IMPORTANTE**: 
- Solo escanea sistemas que te pertenezcan o tengas autorización explícita
- Respeta las políticas de uso de redes y sistemas
- Algunos firewalls pueden detectar escaneos como actividad maliciosa

## 🐛 Solución de Problemas

### Error: "nmap: command not found"
\`\`\`bash
# Ubuntu/Debian
sudo apt-get install nmap

# macOS
brew install nmap

# Windows
# Descargar desde https://nmap.org/download.html
\`\`\`

### Error de permisos
\`\`\`bash
# Ejecutar con sudo si es necesario para ciertos tipos de escaneo
sudo python run-nmap-scan.py
\`\`\`

## 📈 Próximas Mejoras

- [ ] Soporte para múltiples objetivos
- [ ] Exportación a JSON/CSV
- [ ] Integración con bases de datos
- [ ] Dashboard web con Prefect UI
- [ ] Notificaciones por email/Slack
- [ ] Programación de escaneos recurrentes

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo LICENSE para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

**Nota**: Este proyecto es para fines educativos y de administración de sistemas. 
Se realizo en un entorno seguro de dominio de nmap para realizar pruebas.

