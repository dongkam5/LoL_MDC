import React from "react";
import PropTypes from "prop-types";
import { Route} from "react-router";
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import "./styles.module.scss";

import Main from "../Main";
import {connect} from "react-redux";

const App = props => [
  <Routes key={1} />,
];

const Routes = props => (
  <Routes>
      <Route exact path="/" component={Main}/>
  </Routes>
);

const WithRouterSample = () => {
  const params = useParams();
  const location = useLocation();
  const navigate = useNavigate();

  return (
    <>
      <h4>Location</h4>
      <textarea value={JSON.stringify(location, null, 2)} readOnly />

      <h4>Params</h4>
      <textarea value={JSON.stringify(params)} readOnly />

      <button onClick={() => navigate('/')}>홈으로</button>
    </>
  );
};
App.propTypes = {

};
export default WithRouterSample(connect()(App))