const fs = require('fs');
const path = require('path');

module.exports.addAssetLicense = fs.readFileSync(path.join(__dirname, 'addAssetLicense.gql'), 'utf8');
module.exports.addAssetPreviewImage = fs.readFileSync(path.join(__dirname, 'addAssetPreviewImage.gql'), 'utf8');
module.exports.addAssetRelations = fs.readFileSync(path.join(__dirname, 'addAssetRelations.gql'), 'utf8');
module.exports.addAssetTags = fs.readFileSync(path.join(__dirname, 'addAssetTags.gql'), 'utf8');
module.exports.addCollectionAssets = fs.readFileSync(path.join(__dirname, 'addCollectionAssets.gql'), 'utf8');
module.exports.addCustomMetadata = fs.readFileSync(path.join(__dirname, 'addCustomMetadata.gql'), 'utf8');
module.exports.addCustomMetadataPropertyOptions = fs.readFileSync(path.join(__dirname, 'addCustomMetadataPropertyOptions.gql'), 'utf8');
module.exports.createAsset = fs.readFileSync(path.join(__dirname, 'createAsset.gql'), 'utf8');
module.exports.createAssetComment = fs.readFileSync(path.join(__dirname, 'createAssetComment.gql'), 'utf8');
module.exports.createAttachment = fs.readFileSync(path.join(__dirname, 'createAttachment.gql'), 'utf8');
module.exports.createCollection = fs.readFileSync(path.join(__dirname, 'createCollection.gql'), 'utf8');
module.exports.createCustomMetadataProperty = fs.readFileSync(path.join(__dirname, 'createCustomMetadataProperty.gql'), 'utf8');
module.exports.createExternalAsset = fs.readFileSync(path.join(__dirname, 'createExternalAsset.gql'), 'utf8');
module.exports.createFolder = fs.readFileSync(path.join(__dirname, 'createFolder.gql'), 'utf8');
module.exports.createLicense = fs.readFileSync(path.join(__dirname, 'createLicense.gql'), 'utf8');
module.exports.createWorkspaceProject = fs.readFileSync(path.join(__dirname, 'createWorkspaceProject.gql'), 'utf8');
module.exports.deleteAsset = fs.readFileSync(path.join(__dirname, 'deleteAsset.gql'), 'utf8');
module.exports.deleteAttachment = fs.readFileSync(path.join(__dirname, 'deleteAttachment.gql'), 'utf8');
module.exports.deleteCollection = fs.readFileSync(path.join(__dirname, 'deleteCollection.gql'), 'utf8');
module.exports.deleteComment = fs.readFileSync(path.join(__dirname, 'deleteComment.gql'), 'utf8');
module.exports.deleteCustomMetadataProperty = fs.readFileSync(path.join(__dirname, 'deleteCustomMetadataProperty.gql'), 'utf8');
module.exports.deleteFolders = fs.readFileSync(path.join(__dirname, 'deleteFolders.gql'), 'utf8');
module.exports.deleteLicense = fs.readFileSync(path.join(__dirname, 'deleteLicense.gql'), 'utf8');
module.exports.editComment = fs.readFileSync(path.join(__dirname, 'editComment.gql'), 'utf8');
module.exports.installProjectWebhook = fs.readFileSync(path.join(__dirname, 'installProjectWebhook.gql'), 'utf8');
module.exports.inviteProjectUser = fs.readFileSync(path.join(__dirname, 'inviteProjectUser.gql'), 'utf8');
module.exports.moveAssets = fs.readFileSync(path.join(__dirname, 'moveAssets.gql'), 'utf8');
module.exports.moveFolders = fs.readFileSync(path.join(__dirname, 'moveFolders.gql'), 'utf8');
module.exports.removeAssetLicense = fs.readFileSync(path.join(__dirname, 'removeAssetLicense.gql'), 'utf8');
module.exports.removeAssetPreviewImage = fs.readFileSync(path.join(__dirname, 'removeAssetPreviewImage.gql'), 'utf8');
module.exports.removeAssetTags = fs.readFileSync(path.join(__dirname, 'removeAssetTags.gql'), 'utf8');
module.exports.removeCollectionAssets = fs.readFileSync(path.join(__dirname, 'removeCollectionAssets.gql'), 'utf8');
module.exports.removeCustomMetadata = fs.readFileSync(path.join(__dirname, 'removeCustomMetadata.gql'), 'utf8');
module.exports.removeCustomMetadataPropertyOptions = fs.readFileSync(path.join(__dirname, 'removeCustomMetadataPropertyOptions.gql'), 'utf8');
module.exports.reopenAssetComment = fs.readFileSync(path.join(__dirname, 'reopenAssetComment.gql'), 'utf8');
module.exports.replaceAsset = fs.readFileSync(path.join(__dirname, 'replaceAsset.gql'), 'utf8');
module.exports.replyToComment = fs.readFileSync(path.join(__dirname, 'replyToComment.gql'), 'utf8');
module.exports.resolveAssetComment = fs.readFileSync(path.join(__dirname, 'resolveAssetComment.gql'), 'utf8');
module.exports.setCollectionAssets = fs.readFileSync(path.join(__dirname, 'setCollectionAssets.gql'), 'utf8');
module.exports.syncAssetTags = fs.readFileSync(path.join(__dirname, 'syncAssetTags.gql'), 'utf8');
module.exports.uninstallWebhook = fs.readFileSync(path.join(__dirname, 'uninstallWebhook.gql'), 'utf8');
module.exports.updateAsset = fs.readFileSync(path.join(__dirname, 'updateAsset.gql'), 'utf8');
module.exports.updateCollection = fs.readFileSync(path.join(__dirname, 'updateCollection.gql'), 'utf8');
module.exports.updateCustomMetadataProperty = fs.readFileSync(path.join(__dirname, 'updateCustomMetadataProperty.gql'), 'utf8');
module.exports.updateFolder = fs.readFileSync(path.join(__dirname, 'updateFolder.gql'), 'utf8');
module.exports.uploadFile = fs.readFileSync(path.join(__dirname, 'uploadFile.gql'), 'utf8');
