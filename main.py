from flask import Flask, render_template, url_for, redirect
import pafy


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/v/<youtu_id>")
def download(youtu_id):
    try:
        url = "https://www.youtube.com/watch?v=" + youtu_id
        video = pafy.new(url)
        best = video.getbest()
        strm = video.streams
        strm_url_list = []
        strm_res_list = []
        strm_ext_list = []
        for s in strm:
            strm_url_list.append(s.url)
            strm_res_list.append(s.resolution)
            strm_ext_list.append(s.extension)

        stul = strm_url_list
        stres = strm_res_list
        stex = strm_ext_list

        style = url_for('static', filename='style.css')

        return render_template('v.html', title=video.title,
                               desc=video.description,
                               best_url=best.url, ext=best.extension,
                               res=best.resolution, sty=style,
                               yid=youtu_id, author=video.author,
                               views=video.viewcount,
                               rating=round(video.rating),
                               li_do=zip(stul, stres, stex),
                               )
    except:
    	errsty = url_for('static', filename='error.css')
        error_title = "404 Not Found"
        error_string = "404 Not Found. Video Not Available"
        return render_template('v.html', er_tit=error_title,
                               er_str=error_string, erst=errsty)

@app.errorhandler(404)
def error404(e):
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=False, port=33507)
