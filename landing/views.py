from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
import os

def index(request):
    return render(request, "landing/index.html")

@require_GET
def manifest(request):
    manifest_path = os.path.join(settings.BASE_DIR, 'landing/manifest.json')
    with open(manifest_path, 'r') as f:
        return HttpResponse(f.read(), content_type='application/manifest+json')

def serviceworker(request):
    sw_path = os.path.join(settings.BASE_DIR, 'landing/serviceworker.js')
    with open(sw_path, 'r') as f:
        return HttpResponse(f.read(), content_type='application/javascript')

def galeria(request):
    db = settings.FIRESTORE_CLIENT

    docs = db.collection("galeria").stream()

    imagenes = []
    for d in docs:
        imagenes.append({
            "titulo": d.get("titulo"),
            "descripcion": d.get("descripcion"),
            "imagen_url": d.get("imagen_url"),
        })

    return render(request, "landing/galeria.html", {"imagenes": imagenes})

def personajes(request):
    db = settings.FIRESTORE_CLIENT

    docs = db.collection("personajes").stream()

    personajes = []
    for d in docs:
        personajes.append({
            "nombre": d.get("nombre"),
            "rol": d.get("rol"),
            "motivacion": d.get("motivacion"),
            "estilo": d.get("estilo"),
            "detalles": d.get("detalles"),
            "imagen_url": d.get("imagen_url"),
        })

    return render(request, "landing/personajes.html", {"personajes": personajes})

def noticias(request):
    db = settings.FIRESTORE_CLIENT

    docs = db.collection("noticias").order_by("fecha", direction="DESCENDING").stream()

    noticias = []
    for d in docs:
        noticias.append({
            "titulo": d.get("titulo"),
            "contenido": d.get("contenido"),
            "fecha": d.get("fecha"),
            "imagen_url": d.get("imagen_url"),
        })

    return render(request, "landing/noticias.html", {"noticias": noticias})

def acerca(request):
    db = settings.FIRESTORE_CLIENT

    doc = db.collection("historia").document("principal").get()

    historia = None
    if doc.exists:
        historia = {
            "titulo": doc.get("titulo"),
            "contenido": doc.get("contenido"),
        }

    return render(request, "landing/acerca.html", {"historia": historia})

def offline(request):
    return render(request, "landing/offline.html")


