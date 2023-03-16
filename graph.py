import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space
position=st.radio('직군 선택',['POPM','서비스기획자'])
#POPM
df=df=pd.read_excel(r'POPM 기업분류.xlsx',sheet_name=position)
df['대,중견 기업 공고 %']=df['대,중견 기업 공고 %']*100
df['스타트업 공고 %']=df['스타트업 공고 %']*100
df2=df[df['그룹']!='기획 산출물']
df_group=df2.groupby('그룹').sum()
df_group=df_group.drop(['대,중견 기업 공고 %','스타트업 공고 %'],axis=1)
df_group['대기업 공고 %']=round(df_group['대,중견 기업 공고 수']/385*100,2)
df_group['스타트업 공고 %']=round(df_group['스타트업 공고 수']/1854*100,2)
df_group=df_group[df_group.index!='소프트스킬']
#요약 영역
def make_group_graph():
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_group['대기업 공고 %'],
        y=df_group.index,
        name='대기업 공고 %',
        orientation='h',hovertemplate='%{x:2f}%<extra></extra>'
    ))

    fig.add_trace(go.Bar(
        x=df_group['스타트업 공고 %'],
        y=df_group.index,
        name='스타트업 공고 %',
        orientation='h',hovertemplate='%{x:2f}%<extra></extra>'
    ))
    fig.update_layout(
        title='그룹 별 대기업과 스타트업의 요구하는 공고 비율',height=300,margin=dict(l=130,r=20,t=50,b=100)
    )
    return fig
#상세 영역
def make_graph(역량그룹):
    data=df[df['그룹']==역량그룹]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['대,중견 기업 공고 %'],
                         y=data['역량'],name='대기업 공고 %',orientation='h',hovertemplate='%{x:.2f}%<extra></extra>'))
    fig.add_trace(go.Bar(x=data['스타트업 공고 %'],y=data['역량'],name='스타트업 공고 %',orientation='h',hovertemplate='%{x:.2f}%<extra></extra>'))
    fig.update_layout(title=f'{역량그룹}영역 대기업과 스타트업의 요구하는 공고 비율',height=600,margin=dict(l=130,r=20,t=50,b=100))
    return fig
fig2=make_graph('서비스 기획')
fig3=make_graph('프로젝트')
fig4=make_graph('데이터 문해·리서치')
fig5=make_graph('사업·마케팅')
fig1=make_graph('소프트스킬')
fig=make_group_graph()
st.plotly_chart(fig,config={'displayModeBar':False}, use_container_width=True)
st.plotly_chart(fig1,config={'displayModeBar':False}, use_container_width=True)
st.plotly_chart(fig2,config={'displayModeBar':False}, use_container_width=True)
st.plotly_chart(fig3,config={'displayModeBar':False}, use_container_width=True)
st.plotly_chart(fig4,config={'displayModeBar':False}, use_container_width=True)
st.plotly_chart(fig5,config={'displayModeBar':False}, use_container_width=True)
