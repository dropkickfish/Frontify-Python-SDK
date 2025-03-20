const fs = require('fs');
const path = require('path');

module.exports.currentUser = fs.readFileSync(path.join(__dirname, 'currentUser.gql'), 'utf8');
module.exports.account = fs.readFileSync(path.join(__dirname, 'account.gql'), 'utf8');
module.exports.library = fs.readFileSync(path.join(__dirname, 'library.gql'), 'utf8');
module.exports.workspaceProject = fs.readFileSync(path.join(__dirname, 'workspaceProject.gql'), 'utf8');
module.exports.webhooks = fs.readFileSync(path.join(__dirname, 'webhooks.gql'), 'utf8');
module.exports.assets = fs.readFileSync(path.join(__dirname, 'assets.gql'), 'utf8');
module.exports.asset = fs.readFileSync(path.join(__dirname, 'asset.gql'), 'utf8');
module.exports.clientTrackingId = fs.readFileSync(path.join(__dirname, 'clientTrackingId.gql'), 'utf8');
module.exports.creativeTemplate = fs.readFileSync(path.join(__dirname, 'creativeTemplate.gql'), 'utf8');
module.exports.creativeExport = fs.readFileSync(path.join(__dirname, 'creativeExport.gql'), 'utf8');
module.exports.brand = fs.readFileSync(path.join(__dirname, 'brand.gql'), 'utf8');
module.exports.brands = fs.readFileSync(path.join(__dirname, 'brands.gql'), 'utf8');
module.exports.guidelinePage = fs.readFileSync(path.join(__dirname, 'guidelinePage.gql'), 'utf8');
module.exports.node = fs.readFileSync(path.join(__dirname, 'node.gql'), 'utf8');
