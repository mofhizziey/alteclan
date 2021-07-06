import {useForm} from 'react-hook-form'

const SearchComponent = (() => {
    const {handleSubmit, register, errors} = useForm();
    const onSubmit = data => console.log(data)
    const search = {

      borderRadius:"0"
    }
    return (
      <div className="text-center">

      <nav class="navbar navbar-expand-lg navbar-light">
          <div class="container-fluid p-3 justify-content-center">

              <form class="d-flex pl-3" onSubmit={handleSubmit(onSubmit)}>
                <input style={{borderRadius:"0", fontSize:"14px"}} class="form-control me-2" type="search" placeholder="brands, collections, merchandises" aria-label="Search" />
                <button class="pl-3 btn btn-outline-dark" style={search} type="submit">find</button>
              </form>
          </div>
        </nav>

      </div>
    )
  })

export default SearchComponent;
