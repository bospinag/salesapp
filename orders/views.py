from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML, CSS
import tempfile
import os
from .models import Order
from .forms import OrderForm

def print_label(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    html = render_to_string("orders/print.html", {"order": order})

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        HTML(string=html).write_pdf(temp_pdf.name)

    os.system(f'lp -d nelko -o media=Custom.4x6in "{temp_pdf.name}"')

    return redirect("/")

def format_address(text):
    return "\n".join([line.strip() for line in text.strip().splitlines() if line])

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.direccion_formateada = format_address(order.direccion_raw)
            order.save()
            return render(request, 'orders/label.html', {'order': order})
        else:
            print("Form is not valid.", form.errors)
    else:
        form = OrderForm()

    return render(request, 'orders/form.html', {'form': form})

