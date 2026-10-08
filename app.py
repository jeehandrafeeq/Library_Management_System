import streamlit as st
import pandas as pd
from library import Library

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)

# --------------------------
# Session State
# --------------------------

if "library" not in st.session_state:
    st.session_state.library = Library()

library = st.session_state.library

# --------------------------
# CSS
# --------------------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e293b,#111827);
}

header{
visibility:hidden;
}

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

.title{

text-align:center;

font-size:50px;

font-weight:bold;

color:#38bdf8;

padding:15px;

}

.card{

background:rgba(255,255,255,.08);

padding:20px;

border-radius:20px;

backdrop-filter:blur(10px);

box-shadow:0 0 20px rgba(0,0,0,.5);

margin-bottom:20px;

}

.metric{

background:linear-gradient(90deg,#2563eb,#0ea5e9);

padding:20px;

border-radius:15px;

text-align:center;

font-size:22px;

font-weight:bold;

color:white;

}

.stButton>button{

width:100%;

background:#2563eb;

color:white;

border:none;

border-radius:10px;

height:45px;

font-size:18px;

}

.stButton>button:hover{

background:#38bdf8;

transform:scale(1.02);

}
html, body, [class*="css"] {
    color: white !important;
}

label {
    color: white !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #FFD700 !important;
}

p, span, div {
    color: white !important;
}

</style>

""",unsafe_allow_html=True)

st.markdown("<div class='title'>📚 Library Management System</div>",unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:
    st.markdown("<div class='metric'>📚 Total Books<br>"+str(len(library.books))+"</div>",unsafe_allow_html=True)

with col2:

    available=sum(book.is_available for book in library.books)

    st.markdown("<div class='metric'>✅ Available<br>"+str(available)+"</div>",unsafe_allow_html=True)

with col3:

    issued=len(library.books)-available

    st.markdown("<div class='metric'>📕 Issued<br>"+str(issued)+"</div>",unsafe_allow_html=True)

st.write("")

tab1,tab2,tab3,tab4=st.tabs(["➕ Add Book","📖 Issue","📚 Return","📋 View Books"])

# ---------------- Add ----------------

with tab1:

    st.subheader("Add New Book")

    title=st.text_input("Book Title")

    author=st.text_input("Author Name")

    if st.button("Add Book"):

        if title and author:

            library.add_book(title,author)

            st.success("Book Added Successfully")

        else:

            st.warning("Fill all fields")

# ---------------- Issue ----------------

with tab2:

    st.subheader("Issue Book")

    if library.books:

        titles=[book.title for book in library.books]

        selected=st.selectbox("Select Book",titles,key="issue")

        if st.button("Issue"):

            st.success(library.issue_book(selected))

# ---------------- Return ----------------

with tab3:

    st.subheader("Return Book")

    if library.books:

        titles=[book.title for book in library.books]

        selected=st.selectbox("Select Book",titles,key="return")

        if st.button("Return"):

            st.success(library.return_book(selected))

# ---------------- Show Books ----------------

with tab4:

    st.subheader("Library Books")

    if library.books:

        data=[]

        for book in library.books:

            data.append({

                "Title":book.title,

                "Author":book.author,

                "Status":"Available ✅" if book.is_available else "Issued ❌"

            })

        df=pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No Books Added")
