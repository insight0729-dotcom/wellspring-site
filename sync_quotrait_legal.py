# -*- coding: utf-8 -*-
"""Quotrait 약관 사본 맞추기: quotrait 저장소 main 의 legal/ 을 받아 /quotrait/privacy.html·terms.html 로 만든다.
앱 빌드(scripts/build.mjs)와 같은 방식으로 legal/company.json 값을 {{...}} 자리에 채우고,
회사 사이트용으로 세 가지만 손본다: 앱 아이콘 링크 빼기, 맨 위 메뉴에 Wellspring 홈 링크, 영어 문단 주소는 영문 주소.
사용:  python -I sync_quotrait_legal.py            (gh 로그인 필요)
       python -I sync_quotrait_legal.py --src <quotrait 저장소 폴더>   (로컬 사본에서)
구글 인증 파일 googleec603fd399d814ca.html 은 건드리지 않는다."""
import json, pathlib, subprocess, sys

REPO = "insight0729-dotcom/quotrait"
OUT = pathlib.Path(__file__).resolve().parent / "quotrait"
ADDRESS_EN = "602, 6F, Rapa Bldg., 9-1 Gugal-ro 60beon-gil, Giheung-gu, Yongin-si, Gyeonggi-do 16972"


def fetch(path: str, src: pathlib.Path | None) -> str:
    if src:
        return (src / path).read_text(encoding="utf-8")
    r = subprocess.run(["gh", "api", "-H", "Accept: application/vnd.github.raw", f"repos/{REPO}/contents/{path}?ref=main"],
                       capture_output=True, check=True)
    return r.stdout.decode("utf-8")


def main():
    src = pathlib.Path(sys.argv[sys.argv.index("--src") + 1]) if "--src" in sys.argv else None
    c = json.loads(fetch("legal/company.json", src))
    fields = {
        "OPERATOR": c["operator"], "OPERATOR_KO": c["operatorKo"], "REPRESENTATIVE": c["representative"],
        "PRIVACY_OFFICER": c["representative"], "BUSINESS_NUMBER": c["businessNumber"],
        "ECOMMERCE_NUMBER": c["ecommerceNumber"], "ADDRESS": c["address"], "PHONE": c["phone"],
        "SUPPORT_EMAIL": c["supportEmail"],
    }
    css = fetch("legal/_style.css", src)
    for name in ("privacy.html", "terms.html"):
        t = fetch(f"legal/{name}", src).replace("/*STYLE*/", css)
        # 영어 문단의 「{{ADDRESS}}, Republic of Korea」는 영문 주소로
        t = t.replace("{{ADDRESS}}, Republic of Korea", ADDRESS_EN + ", Republic of Korea")
        for k, v in fields.items():
            t = t.replace("{{%s}}" % k, v)
        t = t.replace('<link rel="icon" href="./icons/favicon-48.png" type="image/png">', "")
        t = t.replace("<nav>", '<nav><a href="/">Wellspring</a>', 1)
        if "{{" in t:
            sys.exit(f"{name}: 채우지 못한 자리표시가 남음")
        (OUT / name).write_text(t, encoding="utf-8", newline="\n")
        print("ok", name)


if __name__ == "__main__":
    main()
