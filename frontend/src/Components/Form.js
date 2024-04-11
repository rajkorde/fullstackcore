import React, { useRef, useState } from 'react';


function Form() {

  const inputRef = useRef(null)
  const [answer, setAnswer] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const formSubmitHandler = async event => {
    event.preventDefault();
    // const formData = new FormData(event.target)
    // const payload = Object.fromEntries(formData)
    // console.log(payload["query"])
    // console.log(`Backend url: ${process.env.REACT_APP_API_BASE_URL}`)


    if (inputRef.current == null) return

    const query = inputRef.current.value
    console.log(`Query: ${query}`)

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ "question" : query })
    }

    setIsLoading(true)
    try {
      await fetch(`${process.env.REACT_APP_API_BASE_URL}/ai`, requestOptions)
      .then(response => response.json())
      .then(data => setAnswer(data.answer))
    } catch (err) {
      console.log(err)
      setAnswer(err.message)
    }

    setIsLoading(false)
    //setAnswer("test answer")
  }

  return (
    <>
      <div className='row'>
        <form onSubmit={formSubmitHandler}>
          <div className="mb-3">
            <div id="queryHelp" className="form-text my-2">Enter a query for AI assistant</div>
            <input type="text" className="form-control" id="query1" ref={inputRef} defaultValue="What is the capital of France?"/>

          </div>
          <button type="submit" disabled={isLoading} className="btn btn-primary my-2">{isLoading ? "Searching..." : "Submit"}</button>
        </form>
      </div>
      <div className='row'>
        <div className='col'>
          {answer}
        </div>
      </div>
    </>
  );
}

export default Form