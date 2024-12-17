from app.smiski_quiz import most_common, results

#testing most common
def test_mostcommon():
    answer_list = ["A", "A", "A", "A"]
    assert most_common(answer_list) == "A"

    answer_list = ["A", "D", "C", "D"]
    assert most_common(answer_list) == "D"

    answer_list = ["A", "A", "B", "C"]
    assert most_common(answer_list) == "A"

    answer_list = ["B", "B", "B", "C", "C", "B"]
    assert most_common(answer_list) == "B"

#testing results
#simplified dictionary
smiski_results = [
    {"smiski": "SMISKI DAYDREAMING"},
    {"smiski": "SMISKI PLAYING"},
    {"smiski": "SMISKI NAP TIME"},
    {"smiski": "SMISKI LIFTING"},
    {"smiski": "SMISKI THINKING"},
    {"smiski": "SMISKI HIDING"},
    {"smiski": "RAINBOMB SMISKI"}
]

def test_results():
    answer_list = ["A", "A", "A", "A"]
    assert results(answer_list, smiski_results) == smiski_results[0] #smiski daydreaming

    answer_list = ["A", "D", "C", "D"]
    assert results(answer_list, smiski_results) == smiski_results[3] #smiski lifting

    answer_list = ["A", "A", "B", "C"]
    assert results(answer_list, smiski_results) == smiski_results[0] #smiski daydreaming

    answer_list = ["B", "B", "B", "C", "C", "B"]
    assert results(answer_list, smiski_results) == smiski_results[1] #smiski playing

