_home_work_11_
================

__Search by skills and serial number of candidates.
Everything is implemented on HTTP pages__
--------------------------------------------------

"""
@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    candidate_lower = candidate_name.lower().title()
    name = candidate_by_name(candidate_lower, candidates)
    count = len(name)
    return render_template('search.html', name=name, count=count)
"""
