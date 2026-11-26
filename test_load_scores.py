import pytest
from load_scores import load_scores


def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")


def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []

@pytest.mark.parametrize("점수, 유효한가", [
    (-1, False),
    (0, True),
    (1, True),
    (99, True),
    (100, True),
    (101, False),
])
def test_점수_경계값(tmp_path, 점수, 유효한가):
    임시파일 = tmp_path / "임시.csv"
    임시파일.write_text(f"name,score\n테스트학생,{점수}\n", encoding="utf-8")

    kept, skipped = load_scores(임시파일)

    assert (len(kept) == 1) == 유효한가
    assert len(skipped) == (0 if 유효한가 else 1)

def test_이름이_비어_있으면_건너뛴다():
    kept, skipped = load_scores("weird.csv")
    assert (2, ",90", "이름이 비어 있음") in skipped