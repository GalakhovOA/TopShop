
from .models import CartItem

def cart_items(request):
    cart_items = CartItem.objects.all()
    total_items = sum(item.quantity for item in cart_items)
    return {
        'cart_items': cart_items,
        'total_items': total_items,
    }
