# 🤖🐜 RoboHormiga

[English](#english) | [Español](#español)

## English

RoboHormiga is a collaborative platform for web scraping news sites and creating AI-processed articles. It consists of a Python scraper that collects news data and a Vue 3 frontend that displays dynamic, enhanced articles.

### Project Structure

```
robohormiga/
├── scraper/          # Python web scraper
│   ├── news_scraper.py    # BBC News scraper
│   └── news.json          # Scraped news data
└── frontend/         # Vue 3 web application
    ├── package.json       # Dependencies and scripts
    ├── main.js           # Application entry point
    ├── App.vue           # Main application component
    └── Notice.vue        # Site notice component
```

### Getting Started

#### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

#### Scraper Setup
1. Navigate to the scraper directory:
   ```bash
   cd scraper
   ```

2. Install Python dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the news scraper:
   ```bash
   python news_scraper.py
   ```

#### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser to `http://localhost:5173`

### Features
- 🔍 Web scraping for BBC News headlines
- 🎨 Modern Vue 3 interface with Vite
- 📱 Responsive design
- 🌐 Bilingual support (English/Spanish)

---

## Español

RoboHormiga es una plataforma colaborativa para el web scraping de sitios de noticias y la creación de artículos procesados por IA. Consiste en un scraper de Python que recopila datos de noticias y un frontend de Vue 3 que muestra artículos dinámicos y mejorados.

### Estructura del Proyecto

```
robohormiga/
├── scraper/          # Scraper web en Python
│   ├── news_scraper.py    # Scraper de BBC News
│   └── news.json          # Datos de noticias extraídos
└── frontend/         # Aplicación web Vue 3
    ├── package.json       # Dependencias y scripts
    ├── main.js           # Punto de entrada de la aplicación
    ├── App.vue           # Componente principal de la aplicación
    └── Notice.vue        # Componente de aviso del sitio
```

### Comenzar

#### Prerrequisitos
- Python 3.8+
- Node.js 16+
- npm o yarn

#### Configuración del Scraper
1. Navega al directorio del scraper:
   ```bash
   cd scraper
   ```

2. Instala las dependencias de Python:
   ```bash
   pip install requests beautifulsoup4
   ```

3. Ejecuta el scraper de noticias:
   ```bash
   python news_scraper.py
   ```

#### Configuración del Frontend
1. Navega al directorio del frontend:
   ```bash
   cd frontend
   ```

2. Instala las dependencias:
   ```bash
   npm install
   ```

3. Inicia el servidor de desarrollo:
   ```bash
   npm run dev
   ```

4. Abre tu navegador en `http://localhost:5173`

### Características
- 🔍 Web scraping para titulares de BBC News
- 🎨 Interfaz moderna de Vue 3 con Vite
- 📱 Diseño responsivo
- 🌐 Soporte bilingüe (Inglés/Español)

### License

MIT License - see [LICENSE](LICENSE) file for details.
