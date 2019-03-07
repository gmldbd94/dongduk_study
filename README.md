#운영진 네번째 과제
< 하루에 질문 하나 >
1. 메인 (main.html)
- navbar : login/signup 링크달기
- 메인배경화면 : js로 슬라이드 구현
- 글쓰기버튼

2. 마이페이지 (mypage.html)
- 최근에 쓴 순서대로 글 보여주기

3. 글쓰기 (post.html)
- 질문보여주기 + 새로고침 (새로운 질문 받기)
- 글쓰기 + 사진첨부
- 제출버튼

4. 모아보기 (allpost.html)
- 사용자 이름은 보여주지 않고, 글만 랜덤으로 보여주기
~~~
project [Study]/
   app1 [question]/
      base.html
      main.html
      allpost.html
      post.html
   app2 [accounts]/
      login.html
      signup.html
      mypage.html
~~~

3.5 일지
현재 템플릿 적용해 놓은 상태

구현할 내용
1. 댓글기능
-모델 생성
-form 태그에 적용
-view 만들기
2. 태그 기능
3. session값을 통한 화면 구축

3.6 일지
~~~
pip install Pillow
~~~
모델에서 쉽게 이미지를 다루기위한 api설치해준다.

혹시 에러가 뜬다면 question.migrations 안에있는 initial.py를 지운다.
