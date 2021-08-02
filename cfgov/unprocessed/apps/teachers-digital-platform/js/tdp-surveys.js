const { gradeLevelPage } = require( './survey/grade-level-page' );
const { resultsPage } = require( './survey/result-page' );
const { surveyPage } = require( './survey/survey-page' );

const $ = document.querySelector.bind( document );

const surveys = {
  init() {
    if ( $( '.tdp-survey-results' ) ) {
      resultsPage();
      return;
    }

    if ( $( '.tdp-survey-grade-level' ) ) {
      gradeLevelPage();
      return;
    }

    const el = $( '.tdp-survey-page' );
    if ( el ) {
      surveyPage( el );
    }
  }
};

module.exports = surveys;
