from django.http import HttpResponse
from django.shortcuts import render
from orders.models import OrderPet
from django.contrib.auth.models import User


def orders_history(request):
    user = request.user
    query = OrderPet.objects.filter(user=request.user)
    flag = query.exists()
    status_badge_map = {
        'new':'primary',
        'pending':'warning',
        'delivered':'success',
        'cancelled':'danger',
    }

    #retirve order
    orders = OrderPet.objects.filter(user=user).select_related('order_id','pet').order_by('-order_id__created_at')
    # group by order number
    order_group = {}
    for order in orders:
        order_number = order.order_id.order_number
        if order_number not in order_group:
            order_group[order_number] = {

                'order_date':order.order_id.created_at.date(),
                'status':order.order_id.status,
                'status_badge_map':status_badge_map.get(order.order_id.status,'secondary'),
                'order_number':order_number,
                'grand_total':0,
                'items':[]
            }

        order_group[order_number]['grand_total'] += order.pet_price
        total_price_per_item = order.quantity * order.pet_price
        order_group[order_number]['items'].append({
            'item_name':order.pet.name,
            'item_price':order.pet.price,
            'quantity':order.quantity,
            'total_price_per_item':total_price_per_item

        })


    content = {
        'order_group':order_group.values(),
        'flag':flag

    }
    return render(request,'base/order_history.html',content)