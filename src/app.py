import numpy, dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

server = app.server

CCLabel = {0: '0.0', 0.2: '0.2', 0.4: '0.4', 0.6: '0.6', 0.8: '0.8', 1.0: '1.0'}

app.layout = html.Div([
    html.H1('Contracted Gaussian-Type Orbitals',style={'font-family': 'sans-serif','padding-left': '2.0%','padding-right': '2.0%'}),
    html.H5('Show Best-Fit GTOs:',style={'font-family': 'sans-serif', 'display': 'inline-block','padding-left': '2.0%','padding-right': '2.0%','textAlign': 'left'}),
    html.Div(dcc.Checklist(id='sto_opt',options=[{'label': 'STO-1G', 'value': 'sto1g_opt'},{'label': 'STO-2G', 'value': 'sto2g_opt'},{'label': 'STO-3G', 'value': 'sto3g_opt'}],inputStyle={'display': 'inline-block',"margin-right": "10px"},labelStyle={'display': 'inline-block',"margin-right": "20px",'font-family': 'sans-serif'}),style={'padding-left': '2.0%','padding-right': '2.0%', 'display': 'inline-block','vertical-align': 'middle','textAlign': 'left'}),
    html.Br(),html.Br(),
    html.Div([
        html.Div([html.Div(html.H5('φ₁ = 1.00 exp(-1.000 r²)',style={'font-family': 'sans-serif','textAlign': 'center'}),id='gto_a_title'),
                dcc.Slider(id='gto_a_exp',min=-1.0,max=1.0,step=0.01,value=0.0,marks={i: '{}'.format(10**i) for i in range(-1,2,1)},updatemode='mouseup',tooltip=dict(always_visible=False,placement='bottom'),dots=False),
                html.Br(),
                dcc.Slider(id='gto_a_ccf',min=0.0,max=1.0,step=0.01,value=1.0,marks=CCLabel,updatemode='mouseup',tooltip=dict(always_visible=True,placement='bottom'),dots=False,disabled=False),
    ],style={'width': '30%', 'display': 'inline-block', 'padding-left': '2.0%', 'padding-right': '1.5%'}),
        html.Div([html.Div(html.H5('φ₂ = 1.00 exp(-1.000 r²)',style={'font-family': 'sans-serif','textAlign': 'center'}),id='gto_b_title'),
                dcc.Slider(id='gto_b_exp',min=-1.0,max=1.0,step=0.01,value=0.0,marks={i: '{}'.format(10**i) for i in range(-1,2,1)},updatemode='mouseup',tooltip=dict(always_visible=False,placement='bottom'),dots=False),
                html.Br(),
                dcc.Slider(id='gto_b_ccf',min=0.0,max=1.0,step=0.01,value=1.0,marks=CCLabel,updatemode='mouseup',tooltip=dict(always_visible=True,placement='bottom'),dots=False,disabled=False),
        ],style={'width': '30%', 'display': 'inline-block', 'padding-left': '1.5%', 'padding-right': '1.5%'}),
        html.Div([html.Div(html.H5('φ₃ = 1.00 exp(-1.000 r²)',style={'font-family': 'sans-serif','textAlign': 'center'}),id='gto_c_title'),
                dcc.Slider(id='gto_c_exp',min=-1.0,max=1.0,step=0.01,value=0.0,marks={i: '{}'.format(10**i) for i in range(-1,2,1)},updatemode='mouseup',tooltip=dict(always_visible=False,placement='bottom'),dots=False),
                html.Br(),
                dcc.Slider(id='gto_c_ccf',min=0.0,max=1.0,step=0.01,value=1.0,marks=CCLabel,updatemode='mouseup',tooltip=dict(always_visible=True,placement='bottom'),dots=False,disabled=False),
        ],style={'width': '30%', 'display': 'inline-block', 'padding-left': '1.5%', 'padding-right': '2%'})
        ],style={'width': '100%', 'display': 'inline-block','vertical-align': 'middle'}),
        html.Br(),html.Br(),html.Br(),
        html.Div([
            html.Div([html.H5('STO-1G',style={'font-family': 'sans-serif',"margin-top": "10","margin-bottom": "5",'textAlign': 'center'}),dcc.Graph(id='sto1g',config={'displayModeBar': False})],style={'width': '30%', 'display': 'inline-block', 'padding-left': '2.0%', 'padding-right': '1.5%'}),
            html.Div([html.H5('STO-2G',style={'font-family': 'sans-serif',"margin-top": "10","margin-bottom": "5",'textAlign': 'center'}),dcc.Graph(id='sto2g',config={'displayModeBar': False})],style={'width': '30%', 'display': 'inline-block', 'padding-left': '1.5%', 'padding-right': '1.5%'}),
            html.Div([html.H5('STO-3G',style={'font-family': 'sans-serif',"margin-top": "10","margin-bottom": "5",'textAlign': 'center'}),dcc.Graph(id='sto3g',config={'displayModeBar': False})],style={'width': '30%', 'display': 'inline-block', 'padding-left': '1.5%', 'padding-right': '2%'})
        ],style={'width': '100%', 'display': 'inline-block','vertical-align': 'middle'})
])

@app.callback(
     Output('gto_a_title','children'),
    [Input('gto_a_exp', 'value'),
     Input('gto_a_ccf', 'value')])
def UpdatePhiA(s,c):
    e = pow(10.0,s)
    n = c*pow(2.0*e/numpy.pi,0.75)
    t = html.H5("φ₁ = {0:.2f} exp(-{1:.3f} r²)".format(c,e),style={'font-family': 'sans-serif','textAlign': 'center'})
    return t

@app.callback(
     Output('gto_b_title','children'),
    [Input('gto_b_exp', 'value'),
     Input('gto_b_ccf', 'value')])
def UpdatePhiB(s,c):
    e = pow(10.0,s)
    n = c*pow(2.0*e/numpy.pi,0.75)
    t = html.H5("φ₂ = {0:.2f} exp(-{1:.3f} r²)".format(c,e),style={'font-family': 'sans-serif','textAlign': 'center'})
    return t

@app.callback(
     Output('gto_c_title','children'),
    [Input('gto_c_exp', 'value'),
     Input('gto_c_ccf', 'value')])
def UpdatePhiC(s,c):
    e = pow(10.0,s)
    n = c*pow(2.0*e/numpy.pi,0.75)
    t = html.H5("φ₃ = {0:.2f} exp(-{1:.3f} r²)".format(c,e),style={'font-family': 'sans-serif','textAlign': 'center'})
    return t

@app.callback(
    Output('sto1g', 'figure'),
    [Input('gto_a_exp', 'value'),
     Input('gto_a_ccf', 'value'),
     Input('sto_opt','value')])
def UpdateSTO1G(s,c,sto_opt):
    r = numpy.linspace(0,5.0,num=101)
    e = pow(10.0,s)
    if c == 0.0: cn = 1.0
    else: cn = c / numpy.sqrt(c*c)
    
    o_ea_1g = 0.267
    o_ca_1g = 1.000
    
    o_cna_1g = 1.00
    Opt1g = o_cna_1g*GTO1s(o_ea_1g,r)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=r,y=STO1s(1.0,r) ,mode='lines',line_shape='spline',name='1s STO      ',hoverinfo='none'))
    fig.add_trace(go.Scatter(x=r,y=cn*GTO1s(e,r),mode='lines',line_shape='spline',name='φ₁',hoverinfo='none'))
    if sto_opt is not None:
        if 'sto1g_opt' in sto_opt:
            fig.add_trace(go.Scatter(x=r,y=Opt1g,mode='lines',line_shape='spline',name='Best Fit',hoverinfo='none'))
    fig.update_layout(template='plotly_white',margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},hovermode='closest',autosize=True,legend=dict(orientation='h',yanchor='middle',y=1.0,xanchor='center',x=0.5,bgcolor="rgba(0,0,0,0)",font=dict(size=12)),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis=dict(title='r',tickformat = '.1f',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=8)),yaxis=dict(title='R(r)',tickformat = '.2f',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=8))) 
    return fig

@app.callback(
    Output('sto2g', 'figure'),
    [Input('gto_a_exp', 'value'),
     Input('gto_b_exp', 'value'),
     Input('gto_a_ccf', 'value'),
     Input('gto_b_ccf', 'value'),
     Input('sto_opt','value')])
def UpdateSTO2G(sa,sb,ca,cb,sto_opt):
    r = numpy.linspace(0,5.0,num=101)
    ea = pow(10.0,sa)
    eb = pow(10.0,sb)
    cna = ca / numpy.sqrt(ca*ca+cb*cb)
    cnb = cb / numpy.sqrt(ca*ca+cb*cb)
    Phi = cna*GTO1s(ea,r) + cnb*GTO1s(eb,r)
    
    o_ea_2g = 0.267
    o_ca_2g = 0.975
    o_eb_2g = 0.550
    o_cb_2g = 0.225
    
    o_cna_2g = o_ca_2g / numpy.sqrt(o_ca_2g*o_ca_2g+o_cb_2g*o_cb_2g)
    o_cnb_2g = o_cb_2g / numpy.sqrt(o_ca_2g*o_ca_2g+o_cb_2g*o_cb_2g)
    
    Opt2g = o_cna_2g*GTO1s(o_ea_2g,r) + o_cnb_2g*GTO1s(o_eb_2g,r)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=r,y=STO1s(1.0,r),mode='lines',line_shape='spline',name='1s STO      ',hoverinfo='none'))
    fig.add_trace(go.Scatter(x=r,y=Phi         ,mode='lines',line_shape='spline',name='φ₁ + φ₂',hoverinfo='none'))
    if sto_opt is not None:
        if 'sto2g_opt' in sto_opt:
            fig.add_trace(go.Scatter(x=r,y=Opt2g,mode='lines',line_shape='spline',name='Best Fit',hoverinfo='none'))
    fig.update_layout(template='plotly_white',margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},hovermode='closest',autosize=True,legend=dict(orientation='h',yanchor='middle',y=1.0,xanchor='center',x=0.5,bgcolor="rgba(0,0,0,0)",font=dict(size=12)),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis=dict(title='r',tickformat = '.1f',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=8)),yaxis=dict(title='R(r)',tickformat = '.2f',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=8))) 
    return fig

@app.callback(
    Output('sto3g', 'figure'),
    [Input('gto_a_exp', 'value'),
     Input('gto_b_exp', 'value'),
     Input('gto_c_exp', 'value'),
     Input('gto_a_ccf', 'value'),
     Input('gto_b_ccf', 'value'),
     Input('gto_c_ccf', 'value'),
     Input('sto_opt','value')])
def UpdateSTO3G(sa,sb,sc,ca,cb,cc,sto_opt):
    r = numpy.linspace(0,5.0,num=101)
    ea = pow(10.0,sa)
    eb = pow(10.0,sb)
    ec = pow(10.0,sc)
    cna = ca / numpy.sqrt(ca*ca+cb*cb+cc*cc)
    cnb = cb / numpy.sqrt(ca*ca+cb*cb+cc*cc)
    cnc = cc / numpy.sqrt(ca*ca+cb*cb+cc*cc)
    Phi = cna*GTO1s(ea,r) + cnb*GTO1s(eb,r) + cnc*GTO1s(ec,r)
    
    o_ea_3g = 0.267
    o_ca_3g = 0.955
    o_eb_3g = 0.550
    o_cb_3g = 0.189
    o_ec_3g = 2.000
    o_cc_3g = 0.228
    
    o_cna_3g = o_ca_3g / numpy.sqrt(o_ca_3g*o_ca_3g+o_cb_3g*o_cb_3g+o_cc_3g*o_cc_3g)
    o_cnb_3g = o_cb_3g / numpy.sqrt(o_ca_3g*o_ca_3g+o_cb_3g*o_cb_3g+o_cc_3g*o_cc_3g)
    o_cnc_3g = o_cc_3g / numpy.sqrt(o_ca_3g*o_ca_3g+o_cb_3g*o_cb_3g+o_cc_3g*o_cc_3g)
    
    Opt3g = o_cna_3g*GTO1s(o_ea_3g,r) + o_cnb_3g*GTO1s(o_eb_3g,r) + o_cnc_3g*GTO1s(o_ec_3g,r)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=r,y=STO1s(1.0,r),mode='lines',line_shape='spline',name='1s STO      ',hoverinfo='none'))
    fig.add_trace(go.Scatter(x=r,y=Phi         ,mode='lines',line_shape='spline',name='φ₁ + φ₂ + φ₃',hoverinfo='none'))
    if sto_opt is not None:
        if 'sto3g_opt' in sto_opt:
            fig.add_trace(go.Scatter(x=r,y=Opt3g,mode='lines',line_shape='spline',name='Best Fit',hoverinfo='none'))
    fig.update_layout(template='plotly_white',margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},hovermode='closest',autosize=True,legend=dict(orientation='h',yanchor='middle',y=1.0,xanchor='center',x=0.5,bgcolor="rgba(0,0,0,0)",font=dict(size=12)),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis=dict(title='r',tickformat = '.1f',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=8)),yaxis=dict(title='R(r)',tickformat = '.2f',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=8))) 
    return fig

def GTO1s(s,r):
    return pow(2.0*s/numpy.pi,0.75) * numpy.exp(-s*r*r)

def STO1s(s,r):
    return pow(s*s*s/numpy.pi,0.5) * numpy.exp(-s*r)
    
if __name__ == '__main__':
    app.run_server(debug=False)