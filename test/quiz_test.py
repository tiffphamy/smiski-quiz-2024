from app.smiski_quiz import most_common

def test_mostcommon():
    answer_list = ["A", "A", "A", "A"]
    assert most_common(answer_list) == "A"

    answer_list = ["A", "B", "C", "D"]
    assert most_common(answer_list) == "E"

    answer_list = ["A", "A", "B", "C"]
    assert most_common(answer_list) == "A"

    answer_list = ["B", "B", "B", "C", "C", "B"]
    assert most_common(answer_list) == "B"