import React, { Component } from 'react'

class classclick extends Component {
  render() {
    clickHandler(){
        console.log("Click the button")
    }
    return (
      <div>
        <button onClick={this.clickHandler}>Click Me</button>
      </div>
    )
  }
}

export default classclick 