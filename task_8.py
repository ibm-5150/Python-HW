widget_w = 75
gizmo_w = 112

widget_q = float(input())
gizmo_q = float(input())

order_w = (widget_q * widget_w) + (gizmo_q * gizmo_w)

print("Widgets: "+str(widget_q))
print("Gizmos: "+str(gizmo_q))
print("The total weight of your order is: "+str(order_w)+" gramm")