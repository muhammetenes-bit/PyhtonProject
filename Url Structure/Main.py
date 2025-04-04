import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from anytree import Node, RenderTree

translations = {
    "en": {
        "welcome": "Welcome to the URL Structure Visualizer!",
        "enter_url": "Enter a URL (e.g., https://example.com/path/to/file): ",
        "select_lang": "Select language / Dil seçin / Seleccione idioma / Choisissez la langue:",
        "lang_options": "1. English\n2. Türkçe\n3. Español\n4. Français",
        "invalid_choice": "Invalid choice, defaulting to English.",
        "result": "URL Structure:",
        "dir_listing": "Directory Contents:",
        "error": "Error: Directory listing might be disabled or access denied.",
        "fetching": "Fetching directory contents..."
    },
    "tr": {
        "welcome": "URL Yapısı Görselleştirici'ye hoş geldiniz!",
        "enter_url": "Bir URL girin (örneğin, https://example.com/yol/dosya): ",
        "select_lang": "Dil seçin / Select language / Seleccione idioma / Choisissez la langue:",
        "lang_options": "1. İngilizce\n2. Türkçe\n3. İspanyolca\n4. Fransızca",
        "invalid_choice": "Geçersiz seçim, varsayılan olarak İngilizce kullanılıyor.",
        "result": "URL Yapısı:",
        "dir_listing": "Dizin İçeriği:",
        "error": "Hata: Dizin listeleme kapalı olabilir veya erişim reddedildi.",
        "fetching": "Dizin içeriği alınıyor..."
    },
    "es": {
        "welcome": "¡Bienvenido al Visualizador de Estructura de URL!",
        "enter_url": "Ingrese una URL (ej., https://ejemplo.com/ruta/archivo): ",
        "select_lang": "Seleccione idioma / Dil seçin / Select language / Choisissez la langue:",
        "lang_options": "1. Inglés\n2. Turco\n3. Español\n4. Francés",
        "invalid_choice": "Opción inválida, se usará inglés por defecto.",
        "result": "Estructura de URL:",
        "dir_listing": "Contenido del Directorio:",
        "error": "Error: El listado de directorios podría estar desactivado o el acceso denegado.",
        "fetching": "Obteniendo contenido del directorio..."
    },
    "fr": {
        "welcome": "Bienvenue dans le Visualisateur de Structure d'URL !",
        "enter_url": "Entrez une URL (ex., https://exemple.com/chemin/fichier): ",
        "select_lang": "Choisissez la langue / Dil seçin / Select language / Seleccione idioma:",
        "lang_options": "1. Anglais\n2. Turc\n3. Espagnol\n4. Français",
        "invalid_choice": "Choix invalide, par défaut en anglais.",
        "result": "Structure de l'URL:",
        "dir_listing": "Contenu du Répertoire:",
        "error": "Erreur : Le listage du répertoire est peut-être désactivé ou l'accès est refusé.",
        "fetching": "Récupération du contenu du répertoire..."
    }
}

def get_directory_listing(url, lang):
    try:
        print(translations[lang]["fetching"])
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(translations[lang]["error"])
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a') if a.get('href') not in ['../', './']]
        
        root = Node(urlparse(url).path.rstrip('/').split('/')[-1] or "ROOT")
        for link in links:
            Node(link, parent=root)
        
        print("\n" + translations[lang]["dir_listing"])
        for pre, _, node in RenderTree(root):
            print(f"{pre}{node.name}")
    except Exception as e:
        print(f"{translations[lang]['error']} {str(e)}")

# Dil seçimi
print(translations["en"]["select_lang"])
print(translations["en"]["lang_options"])
lang_choice = input("> ")

lang_map = {"1": "en", "2": "tr", "3": "es", "4": "fr"}
lang = lang_map.get(lang_choice, "en")

if lang_choice not in lang_map:
    print(translations[lang]["invalid_choice"])

# Kullanıcı arayüzü
print("\n" + translations[lang]["welcome"])
url = input(translations[lang]["enter_url"])

# Önce URL yapısını göster
parsed = urlparse(url)
path_parts = [p for p in parsed.path.split('/') if p]

print("\n" + translations[lang]["result"])
print(parsed.netloc)
for i, part in enumerate(path_parts, 1):
    print("│   " * (i - 1) + "└── " + part)

# Dizin listeleme denemesi yap
if url.endswith('/'):
    get_directory_listing(url, lang)
else:
    print("\n" + translations[lang]["error"] + " (URL should end with '/')")