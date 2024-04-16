// sample_spec.js

describe('My First Test', () => {
  it('Visits the homepage', () => {
    cy.visit('https://example.com')
    cy.title().should('include', 'Example Domain')
  })
})