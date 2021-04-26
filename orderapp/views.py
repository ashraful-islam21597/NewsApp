from django.shortcuts import render

from decimal import Decimal

import bd as bd

from django.shortcuts import render, get_object_or_404, redirect

from .models import merchants, Order


def index(request):
    m=merchants.objects.all()
    division=list(bd.divisions)
    district=list(bd.districts)
    l=range(1,6)
    o=Order.objects.all()
    if "submit" in request.POST:
        merchant=request.POST['merchant']
        product_type=request.POST['type']
        weight=request.POST['weight']
        div=request.POST['division']
        dis=request.POST['district']
        thana=request.POST['thana']
        merchantid=request.POST['m_id']

        _merchant=get_object_or_404(merchants, name=merchant)
        if div != "Dhaka":

            if float(weight) <=2:
                charge=130
                cod=round(Decimal(130*(1/100)),4)
                ret_charge=round(Decimal(130*(50/100)),4)
            elif 2<int(weight) <=3:
                charge=150
                cod=round(Decimal(150*(1/100)),4)
                ret_charge=round(Decimal(150*(50/100)),4)
            elif 3<int(weight) <=4:
                charge=170
                cod=round(Decimal(170*(1/100)),4)
                ret_charge=round(Decimal(170*(50/100)),4)
            elif 4<int(weight) <=5:
                charge=190
                cod=round(Decimal(190*(1/100)),4)
                ret_charge=round(Decimal(130*(50/100)),4)
        else:
            if dis == "Dhaka":
                if float(weight) <=2:
                    charge=60
                    cod=0.00
                    ret_charge=0.00
                elif 2<int(weight) <=3:
                    charge=70
                    cod=0.00
                    ret_charge=0.00
                elif 3<int(weight) <=4:
                    charge=80
                    cod=0.00
                    ret_charge=0.00
                elif 4<int(weight) <=5:
                    charge=90
                    cod=0.00
                    ret_charge=0.00
            else:
                if float(weight) <=2:
                    charge=110
                    cod=round(Decimal(110*(1/100)),4)
                    ret_charge=round(Decimal(110*(50/100)),4)
                elif 2<int(weight) <=3:
                    charge=130
                    cod=round(Decimal(130*(1/100)),4)
                    ret_charge=round(Decimal(130*(50/100)),4)
                elif 3<int(weight) <=4:
                    charge=150
                    cod=round(Decimal(150*(1/100)),4)
                    ret_charge=round(Decimal(150*(50/100)),4)

                elif 4<int(weight) <=5:
                    charge=170
                    cod=round(Decimal(170*(1/100)),4)
                    ret_charge=round(Decimal(130*(50/100)),4)


        order=Order(merchant_id=_merchant.id,weight=weight,Division=div,District=dis,Street=thana,Product_type=product_type,merchant_invoice_id=merchantid,Charge=charge,
                    Cod_charge_add=cod,return_charge_add=ret_charge)
        order.save()



        return redirect('/orderlist/',{'order':order})

    return render(request,'index.html',{'m':m,'division':division,'district':district,'l':l})

def orderlist(request):
    o=Order.objects.all()
    return render(request,'create_order.html',{'o':o})
