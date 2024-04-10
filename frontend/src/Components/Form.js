import React from 'react'

function Form() {
  return (
    <>
      <form>
      <div class="mb-3">
        <label for="query1" class="form-label">Enter Query</label>
        <input type="text" class="form-control" id="query1"/>
        <div id="queryHelp" class="form-text">Enter a query for AI assistant</div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    </>
  );
}

export default Form
