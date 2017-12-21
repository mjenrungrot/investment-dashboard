import React from "react";
import { render } from 'react-dom';
import Chart from './components/Chart';
import { getData } from "./components/chartUtils";
import { TypeChooser } from "react-stockcharts/lib/helper";

class ChartComponent extends React.Component {
  componentDidMount() {
    console.log(getData())
    getData().then(data => {
      this.setState({ data })
    })
  }
  render() {
    if(this.state == null){
      return <div>Loading...</div>
    }
    return (
      <TypeChooser>
        {type => <Chart type={type} data={this.state.data} />}
      </TypeChooser>
    );  
  }
}

render(
  <ChartComponent />,
  document.getElementById("equityChart")
)