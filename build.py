# 웰스프링 회사 사이트 페이지 생성기: 머리·꼬리를 한곳에서 관리한다.
# 실행: python -I build.py  (index.html, quotrait/index.html, worklum.html, contact.html 생성)
import pathlib

ROOT = pathlib.Path(__file__).parent
NAV = [("/", "Home"), ("/quotrait/", "Quotrait"), ("/worklum.html", "Worklum"), ("/contact.html", "Contact")]


def page(path, title, desc, body, current):
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{name}</a>' for href, name in NAV
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="/">Wellspring Inc.<span>주식회사 웰스프링</span></a>
  <nav class="nav" aria-label="Main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap cols">
  <div>
    <p><strong>Wellspring Inc.</strong> (주식회사 웰스프링) · CEO Ajung Yoo (대표이사 유아정)</p>
    <p>602, 6F, Rapa Bldg., 9-1 Gugal-ro 60beon-gil, Giheung-gu, Yongin-si, Gyeonggi-do 16972, Republic of Korea</p>
    <p>Business reg. no. 749-81-02704 · E-commerce reg. 2024-용인기흥-2310 · D-U-N-S 695205392</p>
    <p><a href="mailto:admin@wellspring.ai.kr">admin@wellspring.ai.kr</a> · +82 10-9747-3955</p>
    <p>© 2026 Wellspring Inc. All rights reserved.</p>
  </div>
  <nav aria-label="Legal"><a href="/quotrait/privacy.html">Privacy Policy</a><a href="/quotrait/terms.html">Terms of Use</a></nav>
</div></footer>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


page("index.html", "Wellspring Inc. · 주식회사 웰스프링",
     "Wellspring Inc. (주식회사 웰스프링) runs Worklum, a shared office in Yongin, Korea, and develops Quotrait, a reading app for saving and replaying lines from books.",
     """<div class="wrap hero">
  <p class="eyebrow">Yongin, Republic of Korea</p>
  <h1>Spaces and software that help people work and read better.</h1>
  <p class="lead">Wellspring Inc. is a Korean company that runs <strong>Worklum</strong>, a shared office in Yongin, and builds <strong>Quotrait</strong>, a reading app for web, Android and iOS.</p>
  <p class="lead ko">주식회사 웰스프링은 용인에서 공유오피스 「워크룸」을 운영하고, 독서 앱 「Quotrait」를 만드는 회사입니다.</p>
  <div class="hero-img"><img src="/img/hero-1600.webp" alt="Worklum shared office lounge on the 7th floor of Rapa Building, Yongin" width="1600" height="700"></div>
</div>

<section><div class="wrap">
  <h2>What we do</h2>
  <p class="sub">Two businesses, one team, one building in Gugal-dong, Yongin. <span class="ko">하나의 팀이 두 가지 일을 합니다.</span></p>
  <div class="grid">
    <article class="card">
      <div class="pic icon"><img src="/img/quotrait-icon-256.png" alt="Quotrait app icon" width="120" height="120"></div>
      <div class="body">
        <h3>Quotrait — reading app</h3>
        <p>Save the lines you love from books with one photo, listen to them again, and share them as cards.</p>
        <p class="ko">책 속 문장을 사진으로 저장하고, 다시 듣고, 카드로 나누는 독서 앱.</p>
        <a class="more" href="/quotrait/">About Quotrait →</a>
      </div>
    </article>
    <article class="card">
      <div class="pic"><img src="/img/lounge-7f.webp" alt="Worklum lounge" width="800" height="500" loading="lazy"></div>
      <div class="body">
        <h3>Worklum — shared office</h3>
        <p>Private offices, meeting rooms and registered business addresses for small companies and freelancers in Yongin.</p>
        <p class="ko">용인 구갈동의 공유오피스·비상주사무실 「워크룸」.</p>
        <a class="more" href="/worklum.html">About Worklum →</a>
      </div>
    </article>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Company information</h2>
  <p class="sub">회사 정보</p>
  <dl class="facts">
    <dt>Legal name</dt><dd>Wellspring Inc. <span class="ko">(주식회사 웰스프링)</span></dd>
    <dt>CEO</dt><dd>Ajung Yoo <span class="ko">(대표이사 유아정)</span></dd>
    <dt>Address</dt><dd>602, 6F, Rapa Bldg., 9-1 Gugal-ro 60beon-gil, Giheung-gu, Yongin-si, Gyeonggi-do 16972, Republic of Korea<br><span class="ko">경기도 용인시 기흥구 구갈로60번길 9-1, 라파빌딩 6층 602호 (우 16972)</span></dd>
    <dt>Business registration</dt><dd>749-81-02704 <span class="ko">(사업자등록번호)</span></dd>
    <dt>E-commerce registration</dt><dd>2024-용인기흥-2310 <span class="ko">(통신판매업 신고번호)</span></dd>
    <dt>D-U-N-S</dt><dd>695205392</dd>
    <dt>Contact</dt><dd><a href="mailto:admin@wellspring.ai.kr">admin@wellspring.ai.kr</a> · <a href="tel:+821097473955">+82 10-9747-3955</a></dd>
  </dl>
  <div class="btns"><a class="btn primary" href="/contact.html">Contact us</a></div>
</div></section>""", "/")

page("quotrait/index.html", "Quotrait — Save, replay and share lines from books",
     "Quotrait is a reading app by Wellspring Inc. Photograph a page to save the lines you love, listen to them again, and share them as cards.",
     """<div class="wrap hero">
  <div class="app-head">
    <img src="/img/quotrait-icon-256.png" alt="Quotrait app icon" width="96" height="96">
    <div>
      <p class="eyebrow">Reading app · Web, Android, iOS</p>
      <h1 style="margin:0">Quotrait</h1>
    </div>
  </div>
  <p class="lead" style="margin-top:20px">Save the lines you love from books, listen to them again, and share them as cards.</p>
  <p class="lead ko">책에서 만난 좋은 문장을 사진으로 저장하고, 다시 듣고, 카드로 나누는 독서 앱입니다.</p>
  <p style="max-width:680px">You no longer need to find the book again to recall a good line. Photograph the page, pick the lines you want, and they are saved as text you can listen to whenever you like.</p>
</div>

<section><div class="wrap">
  <h2>Features</h2>
  <p class="sub">주요 기능</p>
  <div class="feature-grid">
    <div class="feature"><h3>Save lines</h3><p>Photograph a whole page, then tap or drag over the lines you want, or type them in. Line breaks and hyphenation are cleaned up. Scan the barcode to add the book.</p><p class="ko">페이지를 찍고 원하는 줄만 골라 저장. 바코드로 책 정보 입력.</p></div>
    <div class="feature"><h3>Listen again</h3><p>Choose lines to play, set repeats per line or for the whole list, and adjust reading speed and pauses.</p><p class="ko">저장한 문장을 목소리로 반복해 듣기.</p></div>
    <div class="feature"><h3>Quote cards</h3><p>Share a line as a card with a picture drawn for it, or as a paper memo card, in portrait, story and square sizes.</p><p class="ko">문장에 어울리는 그림을 넣은 카드로 공유.</p></div>
    <div class="feature"><h3>Your lines, your data</h3><p>Choose public or private for each line. Export at any time for free as text, Markdown, CSV or a JSON backup. Signing in is optional.</p><p class="ko">언제든 무료로 내보내기, 로그인은 선택.</p></div>
    <div class="feature"><h3>What your lines say about you</h3><p>See your saved lines sorted into six virtues — wisdom, courage, humanity, justice, temperance and transcendence. An estimate, not a diagnosis.</p><p class="ko">저장한 문장을 여섯 덕목으로 정리.</p></div>
    <div class="feature"><h3>No ads</h3><p>Free for up to 100 saved lines. A monthly membership removes the limit. Available in English and Korean.</p><p class="ko">광고 없음, 무료 100개, 한국어·영어.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Privacy and support</h2>
  <p class="sub">On-device text recognition: photos of book pages are processed on your device and are not uploaded. We do not use ads or tracking tools, and we do not sell personal information.</p>
  <div class="btns">
    <a class="btn" href="/quotrait/privacy.html">Privacy Policy · 개인정보처리방침</a>
    <a class="btn" href="/quotrait/terms.html">Terms of Use · 이용 약관</a>
    <a class="btn primary" href="mailto:admin@wellspring.ai.kr?subject=Quotrait%20support">Support: admin@wellspring.ai.kr</a>
  </div>
</div></section>""", "/quotrait/")

page("worklum.html", "Worklum — Shared office in Yongin · 워크룸",
     "Worklum is a shared office in Gugal-dong, Yongin, run by Wellspring Inc. Private offices, meeting rooms, lounge and registered business addresses.",
     """<div class="wrap hero">
  <p class="eyebrow">Shared office · Yongin</p>
  <h1>Worklum <span class="ko" style="font-weight:500">워크룸</span></h1>
  <p class="lead">A shared office in Gugal-dong, Yongin. Private offices, meeting rooms, a lounge and registered business addresses for small companies, startups and freelancers.</p>
  <p class="lead ko">용인 구갈동 라파빌딩의 공유오피스·비상주사무실입니다. 1인실부터 다인실, 회의실, 라운지, 사업자 주소지 서비스를 운영합니다.</p>
  <div class="btns"><a class="btn primary" href="https://worklum-mo.imweb.me/" rel="noopener">Visit worklum-mo.imweb.me</a></div>
</div>

<section><div class="wrap">
  <h2>Spaces</h2>
  <p class="sub">공간</p>
  <div class="gallery">
    <figure><img src="/img/reception-7f.webp" alt="Worklum entrance and reception" loading="lazy"><figcaption>Entrance · 입구</figcaption></figure>
    <figure><img src="/img/lounge-7f.webp" alt="Worklum lounge" loading="lazy"><figcaption>Lounge · 라운지</figcaption></figure>
    <figure><img src="/img/room1-7f.webp" alt="Private office" loading="lazy"><figcaption>Private office · 1인실</figcaption></figure>
    <figure><img src="/img/meeting-7f.webp" alt="Meeting room" loading="lazy"><figcaption>Meeting room · 회의실</figcaption></figure>
    <figure><img src="/img/booth-7f.webp" alt="Focus booth" loading="lazy"><figcaption>Focus booth · 집중 좌석</figcaption></figure>
    <figure><img src="/img/coffee-7f.webp" alt="Coffee bar" loading="lazy"><figcaption>Coffee bar · 커피 바</figcaption></figure>
    <figure><img src="/img/window-lounge-7f.webp" alt="Window lounge" loading="lazy"><figcaption>Window lounge · 창가 라운지</figcaption></figure>
    <figure><img src="/img/building-exterior.webp" alt="Rapa Building exterior" loading="lazy"><figcaption>Rapa Building · 라파빌딩</figcaption></figure>
  </div>
</div></section>

<section><div class="wrap">
  <h2>Services</h2>
  <p class="sub">서비스</p>
  <div class="feature-grid">
    <div class="feature"><h3>Private offices</h3><p>Furnished rooms for one or more people, with shared lounge, meeting rooms and coffee bar.</p><p class="ko">상주 사무실</p></div>
    <div class="feature"><h3>Business address</h3><p>A registered business address in Yongin for company registration.</p><p class="ko">비상주 사무실(사업자 주소지)</p></div>
    <div class="feature"><h3>Meeting rooms</h3><p>Rooms for meetings, interviews and calls.</p><p class="ko">회의실</p></div>
  </div>
  <dl class="facts" style="margin-top:28px">
    <dt>Location</dt><dd>9-1 Gugal-ro 60beon-gil, Giheung-gu, Yongin-si, Gyeonggi-do <span class="ko">(라파빌딩)</span></dd>
    <dt>Consultation</dt><dd>Weekdays 09:00–18:00 KST <span class="ko">(상담 평일 09~18시)</span></dd>
  </dl>
</div></section>""", "/worklum.html")

page("contact.html", "Contact · Wellspring Inc.",
     "Contact Wellspring Inc. (주식회사 웰스프링): email, phone and office address in Yongin, Korea.",
     """<div class="wrap hero">
  <p class="eyebrow">Contact · 문의</p>
  <h1>Get in touch</h1>
  <p class="lead">For questions about Quotrait, Worklum or partnerships, email or call us. We reply on weekdays.</p>
  <p class="lead ko">Quotrait, 워크룸, 제휴 문의는 메일이나 전화로 연락해 주세요.</p>
</div>
<section><div class="wrap">
  <dl class="facts">
    <dt>Email</dt><dd><a href="mailto:admin@wellspring.ai.kr">admin@wellspring.ai.kr</a></dd>
    <dt>Phone</dt><dd><a href="tel:+821097473955">+82 10-9747-3955</a> <span class="ko">(010-9747-3955)</span></dd>
    <dt>Hours</dt><dd>Weekdays 09:00–18:00 KST <span class="ko">(평일 09~18시)</span></dd>
    <dt>Office</dt><dd>602, 6F, Rapa Bldg., 9-1 Gugal-ro 60beon-gil, Giheung-gu, Yongin-si, Gyeonggi-do 16972, Republic of Korea<br><span class="ko">경기도 용인시 기흥구 구갈로60번길 9-1, 라파빌딩 6층 602호</span></dd>
    <dt>Map</dt><dd><a href="https://map.naver.com/p/search/%EC%9A%A9%EC%9D%B8%EC%8B%9C%20%EA%B8%B0%ED%9D%A5%EA%B5%AC%20%EA%B5%AC%EA%B0%88%EB%A1%9C60%EB%B2%88%EA%B8%B8%209-1" rel="noopener">Naver Map</a> · <a href="https://www.google.com/maps/search/?api=1&amp;query=9-1+Gugal-ro+60beon-gil+Giheung-gu+Yongin" rel="noopener">Google Maps</a></dd>
  </dl>
</div></section>""", "/contact.html")
print("ok")
