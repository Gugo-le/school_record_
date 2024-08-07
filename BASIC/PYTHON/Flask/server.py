from flask import Flask,render_template,request,redirect,send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file
 
app=Flask("JobScrapper")
 
db={
    'python':[]
}
 
 
#@(데코레이터):syntactic sugar(간단해보이는데 안에서 돌아가는 건 복잡한 것..?)
#user가 이 주소의 page를 방문했을때 이 함수를 호출해야하는것을 알게 해줌
#데코레이터는 항상 함수 바로 위에 같이 쓰여야 동작
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/search")
def search():
    keyword=request.args.get("keyword")
    if keyword in db:
        jobs=db[keyword]
    else:
        indeed=extract_indeed_jobs(keyword)
        wwr=extract_wwr_jobs(keyword)
        jobs=indeed+wwr
        db[keyword]=jobs
    return render_template("search.html",keyword=keyword,jobs=jobs)
 
@app.route("/export")
def export():
    keyword=request.args.get("keyword")
    if keyword==None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword,db[keyword])
    #as_attachment=True는 다운로드가 되도록
    return send_file(f"{keyword}.csv",as_attachment=True)
 
app.run("0.0.0.0")