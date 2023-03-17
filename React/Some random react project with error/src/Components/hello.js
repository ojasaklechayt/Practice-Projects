import React from "react";

const Hello  = () => {
/*   return (
        <div>
            <h1>Hello Ojas</h1>
        </div>
    )
*/
return React.createElement('div',{id: 'hello',className: 'dummyclass'}, React.createElement('h1','Hello Oju'))
} 
export default Hello