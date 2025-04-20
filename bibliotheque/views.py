from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LivreForm, Livre
from django.contrib.auth import logout
from django.core.paginator import Paginator

# Create your views here.
def signup(request) :
    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect ('liste_livres')
    else :
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form': form})

def custom_logout(request):
    """Vue personnalisée pour la déconnexion."""
    logout(request)
    return redirect('liste_livres')  # Redirige vers la page d'accueil après déconnexion


@login_required
def livre_create(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            # Ne pas enregistrer tout de suite pour pouvoir modifier l'objet avant
            livre = form.save(commit=False)
            # Associer le livre à l'utilisateur connecté
            livre.ajout_par = request.user
            # Enregistrement final après modification
            livre.save()
            # Redirection vers la liste des livres
            return redirect('liste_livres')
        else:
            # Affiche les erreurs dans la console pour débogage
            print("Erreurs du formulaire :", form.errors)
    else:
        form = LivreForm()
    # Affichage du formulaire vide ou avec erreurs
    return render(request, 'bibliotheque/livre_form.html', {'form': form})


def liste_livres(request):
    query = request.GET.get('q', '')
    if query:
        livres_list = Livre.objects.filter(titre__icontains=query)
    else:
        livres_list = Livre.objects.all().order_by('-date_ajout')
    
    # Pagination
    paginator = Paginator(livres_list, 6)  # 6 livres par page
    page_number = request.GET.get('page')
    livres = paginator.get_page(page_number)
    
    return render(request, 'bibliotheque/livre_list.html', {'livres': livres})

def livre_detail(request,pk) :
    livre = get_object_or_404(Livre, pk=pk)
    return render(request, 'bibliotheque/livre_detail.html', {'livre': livre})

@login_required
def livre_update(request, pk) :
    livre = get_object_or_404(Livre, pk=pk)
    if livre.ajout_par == request.user :
        livre = get_object_or_404(Livre, pk=pk)
        if request.method == 'POST' :
            form = LivreForm(request.POST, instance=livre)
            if form.is_valid() :
                form.save()
            return redirect('liste_livres')
        else :
            form = LivreForm(instance=livre)
    else :
        return redirect('liste_livres')
    return render(request, 'bibliotheque/livre_form.html', {'form': form})

@login_required
def livre_delete(request, pk) :
    livre = get_object_or_404(Livre, pk=pk)
    if livre.ajout_par == request.user :
        if request.method == 'POST' :
            livre.delete()
            return redirect('liste_livres') 
    return render(request, 'bibliotheque/livre_confirm_delete.html', {'livre': livre})