# Kristin Lin
# SoftDev pd09
# Work06: Echo echo echo...
# 2017-10-02

from flask import Flask, render_template, request

echo = Flask(__name__)

# unless something was submitted by form, render form.html, else result.html
@echo.route('/', methods = ['POST', 'GET'])
def root() :
    #username and method
    usr = request.form
    mtd = request.method
    #if anything was submitted via form, POST is called
    if mtd == "POST":
        return render_template('result.html', myusr = usr['usr'], mymtd = mtd)
    return render_template('form.html')

if __name__ == '__main__' :
    echo.debug = True
    echo.run()




