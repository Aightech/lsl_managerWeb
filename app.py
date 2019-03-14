# used to create a web page
import dash
import dash_dangerously_set_inner_html #enable to use raw lines of HTML : However the raw component ids cannot be used for callback.
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

# used to draw some charts
import plotly.plotly as py
import plotly.graph_objs as go

# library to use lab streaming layer : communication
from pylsl import StreamInlet, resolve_stream

# GLOBAL VAR
nb_chanel = 2
data = [[0] for i in range(nb_chanel)]

# Creation of a Dash app
app = dash.Dash('title')
# ---------- START OF THE LAYOUT ----------- #
# the layout of the web page. the layout is created similarly to a html page using dash wrapping function
app.layout = html.Div(
    className="bg-light",
    children=[
        html.Div(className="pcoded-navbar menu-light brand-lightblue active-lightblue",
                 style={
                     "width": "150px",
                     "top": "162px"
                 },
                 children=[
                     html.Div(className="navbar-wrapper",
                              children=[
                                  html.Div(className="navbar-content scroll-div",
                                           children=[
                                               html.Div(className="nav pcoded-inner-navbar",
                                                        children=[
                                                            html.Li(className="nav-item pcoded-menu-caption",
                                                                    children=[
                                                                        html.Label("Options")
                                                                    ]),
                                                            dcc.Input(type="checkbox",
                                                                      className="switch switch-primary d-inline m-r-10",
                                                                      id="box-layouts1"),
                                                            html.Div(className="switch switch-primary d-inline m-r-10",
                                                                     children=[
                                                                         dcc.Input(type="checkbox",
                                                                                   id="box-layouts"),

                                                                         # dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                                                                         #              <label for="box-layouts" class="cr"></label>
                                                                         #              ''')
                                                                     ]),
                                                            html.Label("opt1"),
                                                            html.Button(className="btn btn-rounded btn-success",
                                                                        children="bnt 1",
                                                                        id="bnt_2",
                                                                        value="")
                                                        ])

                                           ])
                              ])
                 ]),
        html.Div(className="container-fluid",
                 style={"background-color": "white"},
                 children=[
                     html.Div(className="row",
                              children=[
                                  html.Div(className="col my-4",
                                           children=[
                                               html.H1(className="cover-heading text-center",
                                                       style={"color": "#3F4D67"},
                                                       children="OTB-400 app")
                                           ]),
                                  html.Div(className="col-md-2",
                                           children=[
                                               html.Img(className="img-fluid d-block mx-auto my-2 logo",
                                                        style={"height": "80px"},
                                                        src="/assets/logo.png")
                                           ]),
                              ])
                 ]),

        html.Div(className="container-fluid",
                 style={
                     "background-color": "#3F4D67",
                     # "height":"50px"
                 },
                 children=[
                     html.Div(className="row",
                              children=[
                                  html.Div(className="col my-1",
                                           children=[
                                               html.H3(className="cover-heading text-center",
                                                       style={"color": "white"},
                                                       children="Menu stuff")
                                           ])
                              ])
                 ]),

        html.Div(className="container my-1",
                 children=[
                     html.Div(className="row",
                              children=[
                                  html.Div(className="col-md-5 col-xl-4",
                                           children=[
                                               html.Div(className="card",
                                                        children=[
                                                            html.Div(className="card-block",
                                                                     children=[
                                                                         html.H6(className="mb-4",
                                                                                 children="Daily Sales"),
                                                                         html.Div(
                                                                             className="row d-flex align-items-center",
                                                                             children=[
                                                                                 html.Div(className="col-9",
                                                                                          children=[
                                                                                              html.H3(
                                                                                                  className="f-w-300 d-flex align-items-center m-b-0",
                                                                                                  children=[
                                                                                                      dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                                                                                                          '''<i class="feather icon-arrow-up text-c-green f-30 m-r-10">'''),
                                                                                                      "36876$"
                                                                                                  ])
                                                                                          ]),
                                                                                 html.Div(className="col-3 text-right",
                                                                                          children=[
                                                                                              html.P(className="m-b-0",
                                                                                                     children="67%")
                                                                                          ])
                                                                             ]),
                                                                         html.Div(className="progress m-t-30",
                                                                                  style={"height": "7px"},
                                                                                  id="bar"
                                                                                  )

                                                                     ])
                                                        ]),
                                               html.Div(className="card",
                                                        children=[
                                                            html.Div(className="card-header",
                                                                     children=[
                                                                         html.H5("data"),
                                                                         html.Div(className="card-header-right",
                                                                                  children=[
                                                                                      html.Div(
                                                                                          className="btn-group card-option",
                                                                                          children=[
                                                                                              html.Button(type="button",
                                                                                                          className="btn dropdown-toggle",
                                                                                                          children=[
                                                                                                              html.I(
                                                                                                                  className="feather icon-more-horizontal")
                                                                                                          ]),
                                                                                              html.Ul(
                                                                                                  className="list-unstyled card-option dropdown-menu dropdown-menu-right",
                                                                                                  children=[
                                                                                                      html.Li(
                                                                                                          className="dropdown-item full-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-maximize"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),
                                                                                                      html.Li(
                                                                                                          className="dropdown-item minimize-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-minus"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),
                                                                                                      html.Li(
                                                                                                          className="dropdown-item reload-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-refresh-cw"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),
                                                                                                      html.Li(
                                                                                                          className="dropdown-item close-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-trash"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),

                                                                                                  ])
                                                                                          ])
                                                                                  ]),
                                                                     ]),
                                                            html.Div(className="card-block",
                                                                     children=[
                                                                         html.Div(id="EMGgraph"),
                                                                         dcc.Graph(id="live-graph"),
                                                                         dcc.Interval(id='inter',
                                                                                      interval=100,
                                                                                      n_intervals=0)
                                                                         # html.Div(id="line-area2",
                                                                         #          className="lineAreaDashboard",
                                                                         #          style={"height": "350"})
                                                                     ])

                                                        ])

                                           ]),
                                  html.Div(className="col-md-6 col-xl-6",
                                           children=[
                                               html.Div(className="card",
                                                        children=[
                                                            html.Div(className="card-header",
                                                                     children=[
                                                                         html.H5("blablablba"),
                                                                         html.Div(className="card-header-right",
                                                                                  children=[
                                                                                      html.Div(
                                                                                          className="btn-group card-option",
                                                                                          children=[
                                                                                              html.Button(type="button",
                                                                                                          className="btn dropdown-toggle",
                                                                                                          children=[
                                                                                                              html.I(
                                                                                                                  className="feather icon-more-horizontal")
                                                                                                          ]),
                                                                                              html.Ul(
                                                                                                  className="list-unstyled card-option dropdown-menu dropdown-menu-right",
                                                                                                  children=[
                                                                                                      html.Li(
                                                                                                          className="dropdown-item full-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-maximize"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),
                                                                                                      html.Li(
                                                                                                          className="dropdown-item minimize-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-minus"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),
                                                                                                      html.Li(
                                                                                                          className="dropdown-item reload-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-refresh-cw"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),
                                                                                                      html.Li(
                                                                                                          className="dropdown-item close-card",
                                                                                                          children=[
                                                                                                              html.A(
                                                                                                                  href="#!",
                                                                                                                  children=[
                                                                                                                      html.Span(
                                                                                                                          children=[
                                                                                                                              html.I(
                                                                                                                                  className="feather icon-trash"),
                                                                                                                              "maximize"
                                                                                                                          ])
                                                                                                                  ])
                                                                                                          ]),

                                                                                                  ])
                                                                                          ])
                                                                                  ]),
                                                                         html.Div(className="card-block",
                                                                                  children=[
                                                                                      html.Div(id="world-low",
                                                                                               style={"height": "450"})
                                                                                  ])
                                                                     ])
                                                        ]),
                                               html.Div(className="row",
                                                        children=[
                                                            html.Div(className="col",
                                                                     children=[
                                                                         dcc.Input(id='input', value="test",
                                                                                   type='text'),
                                                                         html.Div(id='output')
                                                                     ]),
                                                            html.Div(className="col", children=[
                                                                html.Button(className="btn btn-rounded btn-success",
                                                                            children="bnt 1",
                                                                            id="bnt_1",
                                                                            value="")
                                                            ]),
                                                            html.Div(className="switch switch-primary d-inline m-r-10",
                                                                     children=[
                                                                         # html.Label(className="cr",
                                                                         #            children=[
                                                                         #                dcc.Input(type="checkbox",
                                                                         #                          id="box-layouts2")
                                                                         #            ])
                                                                         # dcc.Input(type="checkbox",
                                                                         #           id="box-layouts2"),

                                                                         dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                                                                                        <input type="checkbox" id="box-layouts3">
                                                                                       <label for="box-layouts2" class="cr"></label>
                                                                                       ''')
                                                                     ]),

                                                        ])

                                           ]),
                              ])

                 ]),

    ])
# ---------- END OF THE LAYOUT ----------- #


# ---------- START OF THE CALLBACK ----------- #
# The callback function are used to process the web page event.
# It takes the ID of the input and output dash components implicated
# and process the value of the inputs to return smthing to the output
@app.callback(
    Output(component_id='bar', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    try:
        progress_bar_val = int(input_data)
        return html.Div(id="bargraph",
                        className="progress-bar progress-c-theme",
                        role="progressbar",
                        style={"width": str(progress_bar_val) + "%"}
                        )
    except:
        progress_bar_val = 0
        return html.Div(id="bargraph",
                        className="progress-bar progress-c-theme",
                        role="progressbar",
                        style={"width": str(progress_bar_val) + "%"}
                        )


# This callback is called at a fixed rate thank to the "interval" dash component,
# It is used to update graphic charts for example.
@app.callback(Output('live-graph', 'figure'),
              [Input('inter', 'n_intervals')])
def update_graph_live(n):
    global data
    global T
    global inet
    # TODO put it outside in an dash-independant callback
    # get the chunk of data
    sample, timestamp = inlet.pull_chunk()

    # update the timestamps of the samples of the chunk
    T = T + timestamp
    # gather the datat of the chunk
    for i in range(len(sample)):
        for j in range(len(sample[i])):
            data[j].append(sample[i][j])

    # EXAMPLE TO DRAW MULTI LINES CHARTS
    # traces = []
    # for i in range(len(data)):
    #     traces.append(plotly.graph_objs.Scatter(
    #         x=T,
    #         y=data[i],
    #     ))

    # EXAMPLE TO DRAW HEATMAP CHART
    traces = go.Heatmap(
        z=data
    )

    # return the figure
    return {'data': [traces], 'layout': go.Layout(title="EMG DATA")}
# ---------- END OF THE CALLBACK ----------- #


# Creation of an LSL object
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

# Lauch the web page
if __name__ == "__main__":
    app.run_server(debug=True)

