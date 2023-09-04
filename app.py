from flask import Flask,jsonify,render_template,request,redirect
from database import *

app=Flask(__name__)

app.config['MONGODB_HOST']=url
mydata.init_app(app)

@app.route("/erase/<mod>")
def performDelete(mod):
    collected=laptop.objects(model=mod).first()
    collected.delete()
    return redirect("/list")

@app.route("/update/<mod>",methods=["GET","POST"])
def performEdit(mod):
    if request.method=="GET":
        collected=laptop.objects(model=mod).first()
        return render_template("edit.html",data=collected)
    else:
        model=request.form['model']
        serial=request.form['serial']
        ram=int(request.form['ram'])
        ssd=int(request.form['ssd'])
        price=int(request.form['price'])
        stock=int(request.form['stock'])
        type=request.form['type']

        laptop.objects(model=model).update_one(set__serial=serial,
                                               set__ram=ram,
                                               set__ssd=ssd,
                                               set__price=price,
                                               set__stock=stock,
                                               set__type=type)
        return redirect("/list")



@app.route("/pick/<mod>")
def showRead(mod):
    collected=laptop.objects(model=mod).first()
    return render_template("read.html",data=collected)

@app.route("/new",methods=['GET','POST'])
def newOne():
    if request.method=="GET":
        return render_template("laptop.html")
    else:
        lap=laptop()
        lap.model=request.form['model']
        lap.serial=request.form['serial']
        lap.ram=int(request.form['ram'])
        lap.ssd=int(request.form['ssd'])
        lap.price=int(request.form['price'])
        lap.stock=int(request.form['stock'])
        lap.type=request.form['type']
        
        lap.save()
        
        return redirect("/list")

@app.route("/")
def showHome():
    return render_template("navigation.html")

@app.route("/list")
def listAll():
    collected=laptop.objects.all()
    return render_template("view.html",data=collected)

@app.route("/test")
def checkConnection():
    return jsonify(laptop.objects.all())

@app.route("/shortlist",methods=['GET','POST'])
def performFilter():
    if request.method=="GET":
        return render_template("filter.html")
    else:
        mod=request.form['model']
        tp=request.form['type']
        ram=request.form['ram']
        cost=request.form['price']

        if mod!="" and tp=="Select type" and ram=="" and cost=="":
            collected=laptop.objects(model__startswith=mod)
            return render_template("view.html",data=collected)
        elif mod=="" and tp!="Select type" and ram=="" and cost=="":
            collected=laptop.objects(type__iexact=tp)
            return render_template("view.html",data=collected)
        elif mod=="" and tp=="Select type" and ram!="" and cost=="":
            ram=int(ram)
            collected=laptop.objects(ram__gte=ram)
            return render_template("view.html",data=collected)
        elif mod=="" and tp=="Select type" and ram=="" and cost!="":
            cost=int(cost)
            collected=laptop.objects(price__lte=cost)
            return render_template("view.html",data=collected)
        else:
            return render_template("filter.html")
if __name__=="__main__":
    app.run(debug=True,port=2328)